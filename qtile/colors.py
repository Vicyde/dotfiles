RofiOne = {
    "border_normal":"#808080",
    "border_focus":"#80cbc4",
    "bar_foreground1":"#80cbc4",
    "bar_foreground2":"#98be64",
    "bar_foreground3":"#c1c1c1",
    "bar_foreground4":"#808080",
    "bar_background1":"#273238",
}

def get_color(theme, color, default="#ffffff"):
    if color in theme:
        return theme[color]
    return default
