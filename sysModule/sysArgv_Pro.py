#!/usr/bin/env python3.6

import sys


def func(args) -> None:
    '''

    :return:
    '''
    for i in range(len(args)):
        if i == 0:
            print('Function name is : %s' % args[0])
        else:
            print('argument %d is: %s ' % (i, args[i]))


if __name__ == '__main__':
    func(sys.argv)