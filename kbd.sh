#!/bin/bash


pid=$(ps -C onboard -o pid=)
if [ -z $pid ]
then
onboard
else 
dbus-send --type=method_call --print-reply --dest=org.onboard.Onboard /org/onboard/Onboard/Keyboard org.onboard.Onboard.Keyboard.ToggleVisible > /dev/null
fi