#!/bin/bash

#PLAYERS=$(playerctl -l) # Iterate through all players
PLAYERS="chromium cmus" # Use a list with players, prioritized 

OUTPUT="Silence"

for PLAYER in $PLAYERS; do
  STATUS=$(playerctl status --player=$PLAYER)
  if [[ $STATUS == "Playing" ]]; then
    OUTPUT=$(playerctl metadata --player=$PLAYER --format='{{ trunc(artist,25) }} - {{ trunc(title, 25) }}')
    break;
  fi
done

echo $OUTPUT
