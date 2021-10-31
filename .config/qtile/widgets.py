import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile import widget
from libqtile.utils import guess_terminal
from colors import colors

terminal = guess_terminal()
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

widget_defaults = dict(
    font='MesloLGS NF',
    padding = 0,
    margin = 0,
    fontsize = 30,
    background=colors[0],
    foreground=colors[7]
)
extension_defaults = widget_defaults.copy()

white = "#ffffff";
gray = "#a1a1a1";

def init_widgets_list():
    widgets_list = [
            widget.Sep(
                linewidth = 0,
                padding = 6,
                foreground = colors[2],
                background = colors[0]
            ),
            widget.Image(
                filename = "~/.config/qtile/icons/python-white.png",
                scale = "False",
                background = colors[0], 
                margin=2,
                mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal)}
            ),
            widget.Sep(
                linewidth = 0,
                padding = 6,
                foreground = colors[2],
                background = colors[0]
            ),
            widget.GroupBox(
                font = "MesloLGS Bold",
                fontsize = 22,
                margin_x = 3,
                margin_y = 0,
                padding_x = 3,
                padding_y = 5,
                borderwidth = 3,
                active = white,
                inactive = gray,
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
            widget.Prompt(
                prompt = prompt,
                font = "MesloLGS Bold",
                padding = 10,
                foreground = colors[0],
                background = colors[1]
            ),
            widget.Sep(
                linewidth = 0,
                padding = 40,
                foreground = colors[2],
                background = colors[0]
            ),
            widget.WindowName(
                foreground = colors[6],
                background = colors[0],
                padding = 0
            ),
            widget.Systray(
                background = colors[0],
                padding = 5
            ),
            widget.Sep(
                linewidth = 0,
                padding = 6,
                foreground = colors[0],
                background = colors[0]
            ),
            widget.TextBox(
                text = '',
                font = "MesloLGS NF",
                background = colors[0],
                foreground = colors[2],
                padding = 0,
                fontsize = 18
            ),
            widget.Net(
                interface = "enp9s0",
                format = '{down} ↓↑ {up}',
                foreground = white,
                background = colors[2],
                padding = 5 
            ),
            widget.TextBox(
                text = '',
                font = "MesloLGS NF",
                background = colors[2],
                foreground = colors[3],
                padding = 0,
                fontsize = 18
            ),
            widget.TextBox(
                text = " 🌡",
                padding = 2,
                foreground = white,
                background = colors[3],
                fontsize = 11
            ),
            widget.ThermalSensor(
                foreground = white,
                background = colors[3],
                threshold = 90,
                padding = 5
            ),
            widget.TextBox(
                text='',
                font = "MesloLGS NF",
                background = colors[3],
                foreground = colors[5],
                padding = 0,
                fontsize = 18
            ),
            widget.TextBox(
                text = " ⟳",
                padding = 2,
                foreground = white,
                background = colors[5],
                fontsize = 14
            ),
            widget.CheckUpdates(
                update_interval = 1800,
                distro = "Arch_checkupdates",
                display_format = "{updates} Updates",
                foreground = white,
                mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e yay')},
                
                background = colors[5]
            ),
            widget.TextBox(
                text = '',
                font = "MesloLGS NF",
                background = colors[5],
                foreground = colors[4],
                padding = 0,
                fontsize = 18
            ),
            widget.TextBox(
                text = " 🖬",
                foreground = white,
                background = colors[4],
                padding = 0,
                fontsize = 14
            ),
            widget.Memory(
                foreground = white,
                background = colors[4],
                mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e ytop')},
                padding = 5
            ),
            widget.TextBox(
                text = '',
                font = "MesloLGS NF",
                background = colors[4],
                foreground = colors[5],
                padding = 0,
                fontsize = 18
            ),
            widget.TextBox(
                text = " Vol:",
                foreground = white,
                background = colors[5],
                padding = 0
            ),
            widget.Volume(
                foreground = white,
                background = colors[5],
                padding = 5
            ),
            widget.TextBox(
                text = '',
                font = "MesloLGS NF",
                background = colors[5],
                foreground = colors[4],
                padding = 0,
                fontsize = 18
            ),
            widget.CurrentLayoutIcon(
                custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                foreground = white,
                background = colors[4],
                padding = 0,
                scale = 0.7
            ),
            widget.CurrentLayout(
                foreground = white,
                background = colors[4],
                padding = 5
            ),
            widget.TextBox(
                text = '',
                font = "MesloLGS NF",
                background = colors[4],
                foreground = colors[5],
                padding = 0,
                fontsize = 18
            ),
            widget.Clock(
                foreground = white,
                background = colors[5],
                format = "%A %d %B de %Y - %H:%M "
            ),   
            widget.TextBox(
                text = '',
                font = "MesloLGS NF Bold",
                background = colors[5],
                foreground = colors[0],
                padding = 0,
                fontsize = 18
            ),
            widget.QuickExit(
                default_text = '',
                background = colors[0],
                foreground = colors[6],
                countdown_start = 0,
                padding = 3,
                fontsize = 22
            ),
            widget.Sep(
                linewidth = 0,
                background = colors[0],
                padding = 12
            )
        ]
    return widgets_list

def init_widgets_lite():
    widgets_lite = init_widgets_list()
    del widgets_lite[7:8]   # remove systray
    del widgets_lite[14:16] # remove check updates
    return widgets_lite

def init_widgets_full():
    widgets_full = init_widgets_list()
    return widgets_full



