import os
import subprocess

from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord, DropDown, ScratchPad
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from colors import *

theme=RofiOne

mod = "mod4"

terminal = "alacritty"
browser = "brave" 
rofi = "rofi -show combi"

def run_script(qtile, script):
    run_command = os.path.expanduser('~/.config/qtile/scripts/' + script)
    os.system(run_command)
    
@hook.subscribe.startup_once
def autostart_once():
    lazy.spawn("picom -bc")
    lazy.spawn("emacs --daemon")


keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),

    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

    Key([mod], "e", lazy.spawn('emacsclient -c'), desc="Start emacs"),
    Key([mod], "i", lazy.layout.grow(), desc="Grow the layout"),
    Key([mod], "m", lazy.layout.shrink(), desc="Shrink the layout"),
    Key([mod], "n", lazy.layout.normal(), desc="Set layout to normal size"),

    Key([mod], "q", lazy.function(run_script, 'lock.sh'), desc="Set layout to normal size"),

    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),

    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),

    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    Key([mod], "r", lazy.spawn(rofi), desc="Spawn a command using a prompt widget"),

#    Key([mod], "=", lazy.spawn("amixer sset Master 5%- unmute"), desc="Spawn a command using a prompt widget"),
#    Key([mod], "-", lazy.spawn("amixer sset Master 5%+ unmute"), desc="Spawn a command using a prompt widget"),

    KeyChord([mod], "s", [
        Key([], "t", lazy.spawn(terminal)),
        Key([], "b", lazy.spawn(browser)),
        ],
        name="Spawn"
    )
]

for vt in range(1, 8):
    keys.extend([
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    ])

group_names = [i for i in "1234567890"]

group_labels = ["DEV", "WWW", "SYS", "DOC", "COM", "6", "7", "8", "9", "MISC"]
#group_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]


groups = []
for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            label=group_labels[i],
        )
    )


for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

spSettings = {
        "width":0.6,
        "height":0.8,
        "x":0.2,
        "y":0.1,
        "opacity":0.9,
}

groups.append(ScratchPad("sp", [
    DropDown("volume", "alacritty -e alsamixer", **spSettings),
    DropDown("term", "alacritty --class=scratchpad", **spSettings),
]))

keys.extend([
    Key([mod], "v", lazy.group['sp'].dropdown_toggle('volume')),
    Key([mod], "n", lazy.group['sp'].dropdown_toggle('term')),
])

layoutSettings = {
    "margin":10,
    "border_focus": get_color(theme, "border_focus"),
    "border_normal": get_color(theme, "border_normal"),
}

layouts = [
    layout.MonadTall(ratio=0.65, align=layout.MonadTall._right, **layoutSettings),
    layout.MonadThreeCol(**layoutSettings),
    layout.MonadWide(**layoutSettings),
]

widget_defaults = dict (
    fontsize=18,
    padding=6,
    foreground=get_color(theme, "bar_foreground3"),
)
extension_defaults = widget_defaults.copy()

screens = [ Screen(
        wallpaper="~/Wallpapers/4860933.jpg",
        wallpaper_mode="stretch",
        top=bar.Bar(
            [
                widget.Spacer(length=8),
                widget.CurrentLayoutIcon(),
                widget.TextBox("|", foreground=get_color(theme, "bar_foreground2")),
                widget.GroupBox(
                    highlight_method='line',
                    active=get_color(theme, "bar_foreground1"),
                    this_current_screen_border=get_color(theme, "bar_foreground2"),
                    inactive=get_color(theme, "bar_foreground4"),
                ),
                widget.TextBox("|", foreground=get_color(theme,"bar_foreground2")),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Systray(),
                widget.TextBox("", foreground=get_color(theme, "bar_foreground2")),
                widget.GenPollCommand(cmd="/home/auc/.config/qtile/scripts/disk_free.sh", fmt="{}", update_interval=5),
                widget.TextBox("", foreground=get_color(theme, "bar_foreground2")),
                widget.CPU(format="{freq_current} GHz {load_percent}%"),
                widget.TextBox("", foreground=get_color(theme, "bar_foreground2")),
                widget.Memory(format="{MemPercent}%", measure_mem='G'),
                widget.TextBox("", foreground=get_color(theme, "bar_foreground2")),
                widget.Volume(fmt="{}"),
                widget.TextBox("", foreground=get_color(theme, "bar_foreground2")),
                widget.Clock(format="%a, %b %d - %H:%M"),
                widget.Spacer(length=8),
            ],
            32,
            foreground=get_color(theme, "bar_foreground3"),
            background=get_color(theme, "bar_background1"),
        ),
    ),
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

wl_input_rules = None

wmname = "LG3D"
