#!/bin/sh

# Session
export XDG_SESSION_TYPE=wayland
export XDG_SESSION_DESKTOP=wlroots
export XDG_CURRENT_DESKTOP=wlroots
#export EGLStreamsPath=/usr/lib/nvidia-525.89.02/egl
# export XDG_CURRENT_SESSION=wlroots
# export XDG_CACHE_HOME="/tmp/$USER/.cache"
# export XDG_RUNTIME_DIR=/run/user/$(id -u)

source /usr/local/bin/wayland_enablement.sh

exec start-newm
# WLR_DRM_DEVICES=/dev/dri/card0:/dev/dri/card1 start-newm -d
# WLR_DRM_DEVICES="/dev/dri/card0" start-newm -d
# dbus-run-session start-newm -d
