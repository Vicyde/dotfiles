#!/bin/bash

feh --bg-scale /home/auc/Wallpapers/wp3272764--wallpapers.jpg

if [ "$XDG_SESSION_TYPE" = "x11" ]; then
  picom -bc
fi

/usr/lib/pam_kwallet_init

emacs --daemon
