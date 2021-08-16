#!/bin/bash
setting="$1"
if [[ $setting  = 'pic' ]]
then
	tybg /home/bymyself/Pictures/terminal_background/$2
fi
if [[ $setting  = 'vid' ]]
then 
        tybg /home/bymyself/Pictures/MegaShots/$2
fi
if [[ $setting  = 'loop' ]]
then 
        tybg /home/bymyself/Pictures/Loops/$2
fi
