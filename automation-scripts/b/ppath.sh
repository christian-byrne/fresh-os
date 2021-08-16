#!/bin/bash
base=$(pwd)
file_name=$(ls | grep $1)
echo "$base/$file_name"
