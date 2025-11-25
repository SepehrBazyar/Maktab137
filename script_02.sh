#! /bin/bash

echo "Numbers:"
read -a numbers

summation=$(( numbers[0] + numbers[1] ))

echo "${numbers[0]} + ${numbers[1]} = $summation"

string="HELLO WORLD"

for item in ${numbers[@]}
do
    echo "Item is $item"
done

for (( i=1; i<=10; i++ ))
do
    echo "$i"
done

# for {1..10..2}
# do
#     echo "$i"
# done
