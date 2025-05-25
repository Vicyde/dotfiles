#!/bin/bash

wal -i ~/Wallpapers/wp1813998.jpg 

if [ "$XDG_SESSION_TYPE" = "x11" ]; then
  picom -bc
fi

/usr/lib/pam_kwallet_init

emacs --daemon
