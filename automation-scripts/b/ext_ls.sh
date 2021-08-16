#!/bin/bash
clear;
ls -t --color=always;
printf "\n"
echo 'Current Dir:  \e[2;94m'$(pwd -P)'\e[m\n              \e[2;94m'$(date +"%r")'\e[m'
echo 'Total Space:  \e[1;96m'$(sudo du -hs --block-size=1000000)' Mb\e[m'
echo ' File Count:  \e[1;96m'$(sudo du --inodes -s --block-size=1000000)' Files\e[m\n'