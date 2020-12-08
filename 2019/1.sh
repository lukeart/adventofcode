#!/bin/bash

sum=0
while read weight
do
    echo $weight
    sum=$(( $sum + $weight / 3 - 2 ))
    echo $sum
done
echo $sum