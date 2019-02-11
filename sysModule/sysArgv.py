#!/usr/bin/env python3.6

import sys

if __name__ == '__main__':
    '''
    sys.argv is a list which contains 
    the command-line Arguments passed
    to the Python Script
    '''
    print('this is the Script Name: ', sys.argv[0])
    print('Argv Length :', len(sys.argv))
    print('The Arguments Themselves :', str(sys.argv))