#!/bin/bash

OUTPUT=$(nordvpn status)

STATUS=$(echo "$OUTPUT" | awk '/^Status/ {print $2}')

if [ $STATUS == "Connected" ]; then
  SERVER=$(echo "$OUTPUT" | awk '/^Server/ {$1=""; print $0}')
  echo $SERVER
else
  echo "Disconnected"
fi

