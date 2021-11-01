from libqtile import layout
from colors import colors

layout_theme = {"border_width": 2,
                "margin": 8,
                "border_focus": colors[1],
                "border_normal": colors[5]
                }


layouts = [
    layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.RatioTile(**layout_theme),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    layout.Stack(
        num_stacks=2,
        border_focus=colors[1],
        border_normal=colors[5],
        margin=2,
        border_width=2
    ),
    layout.TreeTab(
         font = "MesloLGS NF",
         fontsize = 10,
         sections = ["FIRST", "SECOND", "THIRD", "FOURTH"],
         section_fontsize = 10,
         border_width = 2,
         bg_color = colors[2],
         active_bg = colors[6],
         active_fg = colors[0],
         inactive_bg = colors[7],
         inactive_fg = colors[2],
         padding_left = 0,
         padding_x = 0,
         padding_y = 5,
         section_top = 10,
         section_bottom = 20,
         level_shift = 8,
         vspace = 3,
         panel_width = 200
         ),
    layout.Floating(**layout_theme)    
]
