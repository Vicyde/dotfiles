#!/bin/bash
# Currently Playing Script
# by Vicyde


# A script that iterates through all values in it's variable, to determine if
# it is a player, playing something. If it is, we echo what it is playing and
# exit the script.
iterate_players() {
  for PLAYER in $1; do
    STATUS=$(playerctl status --player=$PLAYER)
    if [[ $STATUS == "Playing" ]]; then
      OUTPUT=$(playerctl metadata --player=$PLAYER --format='{{ trunc(artist,25) }} - {{ trunc(title, 25) }}')
      echo $OUTPUT
      exit
    fi
  done
}

# First, iterate through a list of prioritized players
iterate_players "chromium cmus"

# Still in the script? Then we have no prioritized player found, so interate
# through all of them
iterate_players $(playerctl -l)

# Still nothing? Then it must be silent!
echo "Silence"


