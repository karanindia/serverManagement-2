#!/usr/bin/env bash
for i in {100..110}; do
    ping -c 1 192.168.1.$i > /dev/null || echo "192.168.1.$i is Down"
done
