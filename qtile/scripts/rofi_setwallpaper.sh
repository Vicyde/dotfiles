#!/bin/bash

wallpapers=/home/auc/Wallpapers/

choice=$(ls $wallpapers | rofi -dmenu -p "Select wallpaper") || exit 0

if [[ choice != "" ]]; then
  rm $wallpapers"active"
  ln -s $wallpapers$choice $wallpapers"active"
  wal -i $wallpapers"active"
  qtile cmd-obj -f restart
fi

