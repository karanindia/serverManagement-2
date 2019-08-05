#!/usr/bin/env bash
if [ -z $1 ]; then
    echo -n "Enter Your Name: "
    read name
else
    echo $1
fi
