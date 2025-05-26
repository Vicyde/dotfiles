#!/bin/bash

pactl set-default-sink $(pactl list short sinks | awk '{print $2}' | rofi -dmenu -no-fixed-num-lines -p "Audio sink")

