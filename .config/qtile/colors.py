import os
from libqtile.lazy import lazy

# custom Colors from pywal
colors = []
cache=os.path.expanduser('~/.cache/wal/colors')
def load_colors(cache):
    with open(cache, 'r') as file:
        for i in range(8):
            colors.append(file.readline().strip())
    colors.append('#ffffff')
    lazy.reload()
load_colors(cache)
# !end custom colors from pywal


