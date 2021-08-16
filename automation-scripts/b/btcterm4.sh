#!/bin/bash

xdotool key ctrl+shift+f
sleep .3
xdotool key ctrl+shift+h
sleep .3
xdotool key ctrl+shift+j
sleep .3
xdotool key alt+j
sleep .3
xdotool key ctrl+shift+j
foo=$(shuf -i1-120 -n400)
boo=~/bash_scripts/quote_returner 
$boo $foo