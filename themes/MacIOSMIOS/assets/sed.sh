#!/bin/sh
sed -i \
         -e 's/#e5e5e5/rgb(0%,0%,0%)/g' \
         -e 's/#1a1a1a/rgb(100%,100%,100%)/g' \
    -e 's/#d5d5d5/rgb(50%,0%,0%)/g' \
     -e 's/#80ccf2/rgb(0%,50%,0%)/g' \
     -e 's/#e5e5e5/rgb(50%,0%,50%)/g' \
     -e 's/#1a1a1a/rgb(0%,0%,50%)/g' \
	$@
