'''

 ██████╗ ████████╗██╗██╗     ███████╗
██╔═══██╗╚══██╔══╝██║██║     ██╔════╝
██║   ██║   ██║   ██║██║     █████╗  
██║▄▄ ██║   ██║   ██║██║     ██╔══╝  
╚██████╔╝   ██║   ██║███████╗███████╗
 ╚══▀▀═╝    ╚═╝   ╚═╝╚══════╝╚══════╝
                                 
'''


import os
import subprocess

from typing import List  # noqa: F401

from libqtile import hook, layout
from libqtile.config import Click, Drag, Match
from libqtile.lazy import lazy

# Config files import
from colors import colors
from widgets import init_widgets_list, init_widgets_lite, init_widgets_full
from screens import *
from layouts import layouts
from groups import groups
from keys import keys, mod

# groups binding keys
from libqtile.dgroups import simple_key_binder
dgroups_key_binder = simple_key_binder("mod4")

# init screens
if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_full()
    widgets_screen2 = init_widgets_lite()

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# Cofigure autostart script
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
