#!/usr/bin/env python3.6

import sys

if __name__ == '__main__':
    sys.stdout.write('Hello \n')
    a = input('please Enter A Number: ')
    sys.stdout.write(a + '\n')
    print("type in value: ", sys.stdin.readline()[0:])
