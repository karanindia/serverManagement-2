#!/usr/bin/env bash
case $1 in
    start)
        echo $0 is starting;;
    stop)
        echo $0 is stoped;;
    status)
        echo echo $0 status;;
    *)
        echo "you should start | stop | status";;
esac

