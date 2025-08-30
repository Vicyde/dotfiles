#!/bin/bash

GROUP=$1
LABEL=$(rofi -dmenu -p "Label")

qtile cmd-obj -o group $GROUP -f set_label --args "$GROUP: $LABEL"

