#!/bin/bash

OLDIFS=$IFS
IFS=','
declare -a master array
read -ra master

for j in {0..99}
do
    for i in {0..99}
    do
        array=("${master[@]}")
        #declare -p array
        array[1]=$i
        array[2]=$j

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
        #echo ${array[0]}
        if [ ${array[0]} -eq 19690720 ]
        then
            echo $(( 100 * $i + $j ))
        fi
    done
done
IFS=$OLDIFS