#!/usr/bin/env python3.6
import os


def read_file():
    '''
        Reads a csv file and treat each line as list of values
        which will be sent to a shell script as parameters
    :return: Nothing
    '''
    with open('mtn2_test_service.csv') as file:
        next(file)
        for i in file.readlines():
            try:
                os.system(f"./stop-notification-service.sh {i.split(',')[3]} {i.split(',')[4]} {i.split(',')[1]}")
            except OSError as e:
                print(e)
                pass
            finally:
                file.close()


if __name__ == '__main__':
    read_file()
