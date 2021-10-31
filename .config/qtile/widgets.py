from libqtile import widget
from colors import colors

widget_defaults = dict(
    font='MesloLGS NF',
    fontsize=14,
    padding=3
)
extension_defaults = widget_defaults.copy()

def init_widgets_list():
    widgets_list = [
                widget.CurrentLayout(),
                widget.GroupBox(
                    font = "MesloLGS Bold",
                    fontsize = 30,
                    margin_x = 3,
                    margin_y = 0,
                    padding_x = 3,
                    padding_y = 5,
                    borderwidth = 3,
                    active = colors[7],
                    inactive = colors[2],
                    rounded = "false",
                    highlight_color = colors[1],
                    highlight_method = "line",
                    this_current_screen_border = colors[5],
                    this_screen_border = colors [4],
                    other_current_screen_border = colors[6],
                    other_screen_border = colors[4],
                    foreground = colors[2],
                    background = colors[0]
                ),
                widget.Prompt(),
                widget.WindowName(),
                widget.TextBox("Press &lt;M-r&gt; to spawn", foreground=colors[6]),
                widget.Systray(),
                widget.Clock(format='%A %d %B de %Y | %H:%M'),
                widget.QuickExit(),
            ]
    return widgets_list

def init_widgets_lite():
    widgets_lite = init_widgets_list()
    del widgets_lite[5:6]   # remove systray
    return widgets_lite

def init_widgets_full():
    widgets_full = init_widgets_list()
    return widgets_full



