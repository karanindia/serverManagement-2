#!/usr/bin/env bash

echo "you have entered $# arguments"
echo $@
for i in $@
do
    echo $i
done
