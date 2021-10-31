from libqtile.config import Screen 
from libqtile import bar
from widgets import init_widgets_lite, init_widgets_full

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_full(), opacity=1.0, size=24)),
            Screen(top=bar.Bar(widgets=init_widgets_lite(), opacity=1.0, size=24))]

