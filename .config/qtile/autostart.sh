#!/bin/sh


# screen pos
xrandr --output HDMI-0 --primary --mode 1920x1080 --pos 1920x0 --rotate normal --output DP-0 --off --output DP-1 --off --output HDMI-1 --mode 1920x1080 --pos 0x0 --rotate normal --output DP-2 --off --output DP-3 --off

# force DPI as propietary nvidia driver UseEdidDpi fails to detect correct DPI
xrandr --dpi 96

lxsession & 
picom --experimental-backends --backend glx --xrender-sync-fence &
volumeicon &
udiskie -t &
nm-applet &

# wal color settings
#wal -i "$(< "${HOME}/.cache/wal/wal")"
wal -R

