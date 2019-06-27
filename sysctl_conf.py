#! /usr/bin/env python3.6

import subprocess
import argparse
import os


class parser:
    """
    Parsing command line arguments with the argparse
    """

    def __init__(self):
        """
        Setting and Parsing arguments
        """
        self.parser = argparse.ArgumentParser(description='sysctl Config Helper')
        # sets the input Parameter
        self.parser.add_argument('input',
                                 type=str,
                                 help='Kernel Tunables Names')
        self.parser.add_argument('-p', '--pattern',
                                 type=str,
                                 help='Pattern for Finding Kernel Tunable')
        self.parser.add_argument('-t', '--tunable',
                                 type=str,
                                 help='Exact Name of the Kernel Tunable')
        self.args = self.parser.parse_args()

    def propagate_args(self) -> argparse:
        """
         Returns the custom logger for use in others classes
        :param self: Set and Parsed instance of argparse
        :return argparse: The arguments will be propagated to the caller
        """
        return self.args


# Instantiating arg_parser class
args = parser().propagate_args()


def read_sysctl():
    try:
        subprocess.Popen(['sysctl', '-p'])
    except OSError as ex:
        print(ex)


def read_parameters(pattern):
    try:
        a = subprocess.Popen(['sysctl', '-a'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        b = subprocess.Popen(['grep', pattern], stdout=subprocess.PIPE, stdin=a.stdout, stderr=subprocess.PIPE)
        print(bytes.decode(b.communicate()[0], 'utf-8'))
    except OSError as ex:
        print(ex)


def write(tunable):
    try:
        os.system(f'echo {tunable} >> /etc/sysctl.conf')
    except OSError as ex:
        print(ex)


if __name__ == '__main__':
    if args.input == 'read':
        """
            Run it as follows:
                #./sysctl_conf.py read
        """
        read_sysctl()
    elif args.input == 'read-pattern':
        """
            Run it as follows:
                #./sysctl_conf.py read-pattern -p random
        """
        read_parameters(args.pattern)
    elif args.input == 'write':
        write('vm.swappiness=40')
