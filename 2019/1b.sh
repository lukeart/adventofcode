#!/bin/bash

sum=0
while read weight
do
    echo $weight
    fuel=$(( $weight / 3 - 2 ))
    while [ $fuel -gt 0 ]
    do
        sum=$(( $sum + $fuel ))
        fuel=$(( $fuel / 3 - 2 ))
    done
    echo $sum
done
echo $sum