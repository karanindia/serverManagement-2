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


def write_security():
    tunables = ['fs.suid_dumpable=0',
                'kernel.randomize_va_space=2',
                'net.ipv4.ip_forward=0',
                'net.ipv4.conf.all.send_redirects=0',
                'net.ipv4.conf.default.send_redirects=0',
                'net.ipv4.conf.all.accept_source_route=0',
                'net.ipv4.conf.default.accept_source_route=0',
                'net.ipv4.conf.all.accept_redirects=0',
                'net.ipv4.conf.default.accept_redirects=0',
                'net.ipv4.conf.all.secure_redirects=0',
                'net.ipv4.conf.default.secure_redirects=0',
                'net.ipv4.conf.all.log_martians=1',
                'net.ipv4.conf.default.log_martians=1',
                'net.ipv4.icmp_echo_ignore_broadcasts=1',
                'net.ipv4.icmp_ignore_bogus_error_responses=1',
                'net.ipv4.conf.all.rp_filter=1',
                'net.ipv4.conf.default.rp_filter=1',
                'net.ipv4.tcp_syncookies=1',
                'net.ipv6.conf.all.accept_ra=0',
                'net.ipv6.conf.default.accept_ra=0',
                'net.ipv6.conf.all.accept_redirects=0',
                'net.ipv6.conf.default.accept_redirects=0']
    try:
        with open('/etc/sysctl.d/90-security.conf', 'w+') as conf_file:
            for i in tunables:
                conf_file.write(i + '\n')
        os.system('sysctl -w net.ipv4.route.flush=1 && sysctl -p /etc/sysctl.d/90-security.conf')
    except OSError as ex:
        print(ex)


def write(tunable: str):
    existing_value = ''
    try:
        with open('/etc/sysctl.conf', 'r') as sysctl_file:
            for i in sysctl_file:
                if str(i.split('=')[0]) == tunable.split('=')[0]:
                    existing_value = str(i.strip('\n'))
                    break
                else:
                    continue
        if existing_value != '':
            os.system(f'sudo sed -i "s/{existing_value}/{tunable}/g" /etc/sysctl.conf && sysctl -p')
            print(f'{existing_value} is replaced by {tunable}')
        else:
            os.system(f'echo {tunable} >> /etc/sysctl.conf && sysctl -p')
            print(f'value {tunable} has been added to sysctl.conf')
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
        """
            Run as follows:
                #./sysctl_conf.py write tunable
        """
        # outPut = subprocess.Popen(['sysctl', '-p'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # if len(bytes.decode(outPut.communicate()[0], 'utf-8').split('\n')) > 0:
        write(args.tunable)
    elif args.input == 'security':
        write_security()
