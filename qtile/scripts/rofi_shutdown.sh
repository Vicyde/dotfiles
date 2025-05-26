#!/bin/bash

killprocess() {
  pid=$(ps -u $USER -o pid,comm | awk 'NR > 1' | rofi -dmenu -p "Process to kill" | awk '{print $1}') 
  if [[ $pid != "" ]]; then
    kill -9 $pid
    notify-send "Kill" "Process $pid killed."
  fi
}


choice=$(printf "Kill Process|Reboot|Suspend|Hibernate|Shutdown" | rofi -sep "|" -dmenu -l 5 -p "Choose")
case $choice in
  "Kill Process") killprocess ;;
  "Reboot") systemctl reboot ;;
  "Suspend") systemctl suspend ;;
  "Hibernate") systemctl hibernate ;;
  "Shutdown") systemctl poweroff ;;
  *) exit ;;
esac

