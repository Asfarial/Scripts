#!/bin/bash

#Get status
status=$(xinput list-props "SynPS/2 Synaptics TouchPad" | grep 176)

#Check Touchpad`s toggled status and change status to opposite
if [ "$status" == "	Device Enabled (176):	0" ]
then
xinput enable "SynPS/2 Synaptics TouchPad"
else
xinput disable "SynPS/2 Synaptics TouchPad"
fi

# Additional
# Run the Terminal
# chmod 774 ./touchpad_toogle.sh
# cp ./touchpad_toggle.sh /usr/bin/touchpad_toggle
# Make shortcut to execute command 'touchpad_toogle'