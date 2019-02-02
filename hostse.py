#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import argparse
import re

# Custom args
parser = argparse.ArgumentParser(description='Key Value')
parser.add_argument('key', type=str, help='Search Key')
arg = parser.parse_args()


def search_data(search_key: str) -> None:
    """
    Searches the key in each row of the file
    by re class, and prints the entire line
    containing the search_key.
    :param search_key: A string key to search
    :return: none
    """
    try:
        with open('/etc/hosts', mode='r') as host_list:
            for row in host_list:
                if re.search(search_key, str(row)):
                    print(row)
    except EnvironmentError as e:
        print(str(e))


if __name__ == '__main__':
	search_data(arg.key)
