#!/bin/sh


# screen pos
xrandr --output HDMI-0 --primary --mode 1920x1080 --pos 1920x0 --rotate normal --output DP-0 --off --output DP-1 --off --output HDMI-1 --mode 1920x1080 --pos 0x0 --rotate normal --output DP-2 --off --output DP-3 --off

lxsession & 
picom --experimental-backends --backend glx --xrender-sync-fence &
volumeicon &
nm-applet &

# wal color settings
#wal -i "$(< "${HOME}/.cache/wal/wal")"
wal -R

