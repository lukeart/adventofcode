#!/bin/sh

OLDIFS=$IFS
IFS=','

declare -a array

read -ra array

for i in "${array[@]}"
do
    echo $i
done
IFS=$OLDIFS