#!/bin/bash

INPUT=/dev/stdin
OLDIFS=$IFS
IFS=','

declare -a array
read -ra array

array[1]=12
array[2]=2

pos=0
while [ ${array[$pos]} -ne 99 ]
do
    op1=${array[$pos+1]}
    op2=${array[$pos+2]}
    case ${array[$pos]} in
        1)
            val=$(( ${array[$op1]} + ${array[$op2]} ))
            ;;
        2)
            val=$(( ${array[$op1]} * ${array[$op2]} ))
            ;;
        *)
            ;;
    esac
    dest=${array[$pos+3]}
    array[$dest]=$val
    pos=$(( $pos + 4 ))
done
echo ${array[0]}
IFS=$OLDIFS