#! /bin/bash

number=$1

if [ $number -gt 10 ];
then
    echo "Greater"
elif [ $number -eq 10 ];
then
    echo "Equal"
else
    echo "Less"
fi

echo "END"
