from libqtile.lazy import lazy

RofiOne = {
    "border_normal":"#808080",
    "border_focus":"#80cbc4",
    "bar_foreground1":"#80cbc4",
    "bar_foreground2":"#98be64",
    "bar_foreground3":"#c1c1c1",
    "bar_foreground4":"#808080",
    "bar_background1":"#273238",
}

# It is possible to use a theme (Like RofiOne), or use pywall.
# For the latter: set theme to 'wal'.
def get_color(theme, color, default="#ffffff"):
    if theme == 'wal':
        match color:
            case "border_normal":   return colors[4] # Border normal
            case "border_focus":    return colors[3] # Border focus
            case "bar_foreground1": return colors[3] # Active Font
            case "bar_foreground2": return colors[3] # Icons and active bar
            case "bar_foreground3": return colors[2] # Status and window title
            case "bar_foreground4": return colors[1] # Inactive bars
            case "bar_background1": return colors[0] # Background bar
    else:
        if color in theme:
            return theme[color]

    return default

colors = []
def init_colors(cache):
    with open(cache, 'r') as file:
        for i in range(8):
            colors.append(file.readline().strip())
    colors.append('#ffffff')
    lazy.reload()

