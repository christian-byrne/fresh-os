#!/bin/bash
nohup nautilus ~/Desktop >/dev/null &
disown
foo=$(shuf -i1-120 -n400)
boo=~/bash_scripts/quote_returner 
$boo $foo