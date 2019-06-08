#!/usr/bin/env python3.6

import subprocess


def func1():
    '''
    This Function is intended to Generate 20 File Names for
    first 20 Days of April.
    :return: No Return Value, the Function just Prints the Results
    '''
    test = 'vas-games-access.log-201904'
    ext = '.gz'
    for i in range(1, 21):
        if i < 10:
            day = '0' + str(i)
            print(test + day + ext)
        else:
            day = str(i)
            print(test + day + ext)


dates = ['vas-games-access.log-20190321.gz',
         'vas-games-access.log-20190322.gz',
         'vas-games-access.log-20190323.gz',
         'vas-games-access.log-20190324.gz',
         'vas-games-access.log-20190325.gz',
         'vas-games-access.log-20190326.gz',
         'vas-games-access.log-20190327.gz',
         'vas-games-access.log-20190328.gz',
         'vas-games-access.log-20190329.gz',
         'vas-games-access.log-20190330.gz',
         'vas-games-access.log-20190331.gz',
         'vas-games-access.log-20190401.gz',
         'vas-games-access.log-20190402.gz',
         'vas-games-access.log-20190403.gz',
         'vas-games-access.log-20190404.gz',
         'vas-games-access.log-20190405.gz',
         'vas-games-access.log-20190406.gz',
         'vas-games-access.log-20190407.gz',
         'vas-games-access.log-20190408.gz',
         'vas-games-access.log-20190409.gz',
         'vas-games-access.log-20190410.gz',
         'vas-games-access.log-20190411.gz',
         'vas-games-access.log-20190412.gz',
         'vas-games-access.log-20190413.gz',
         'vas-games-access.log-20190414.gz',
         'vas-games-access.log-20190415.gz',
         'vas-games-access.log-20190416.gz',
         'vas-games-access.log-20190417.gz',
         'vas-games-access.log-20190418.gz',
         'vas-games-access.log-20190419.gz',
         'vas-games-access.log-20190420.gz']
servs = ['8228',
         '201020',
         '201025',
         '2010200',
         '7SOBH',
         'AGHAN',
         'ESHGHD',
         'ETN',
         'FH',
         'HAFEZA',
         'HAMSARANJ',
         'KHABN',
         'KHANOMN',
         'KOJA',
         'MHSH',
         'NOSHIDAN',
         'SHANS',
         'SHD',
         'WHO',
         'YADET',
         '7SOBH',
         'ADBM',
         'AGHAN',
         'ALODEGI',
         'BACHEN',
         'BIORHYTHM',
         'CHAGH',
         'DEGHAT',
         'ENTEZARD',
         'ESHGHD',
         'ETN',
         'FAMIL',
         'FARHANG',
         'HAFEZA',
         'ISLM',
         'KABEDS',
         'KHANOMN',
         'KIMIT',
         'LAGHAR',
         'MASO',
         'MOHARAM',
         'MORMO',
         'NOSHIDAN',
         'OTOL',
         'PANA',
         'POUST',
         'RAZMA',
         'SHANS',
         'TAGHZI',
         'TAHUSH',
         'VALED',
         'WHO',
         'YADET']


def func2():
    '''
    This Function Executes a Command with subprocess
    :return: No Result Value, The Function prints the stdout of the Linux Command
    '''
    a, stdout_value = 0, 0
    for i in servs:
        for j in dates:
            a = subprocess.Popen(['sudo', 'zgrep', '-ic', i, j], stdout=subprocess.PIPE)
            stdout_value += int(a.communicate()[0])
        print(i, repr(stdout_value))
        print('jjh', end='')
        stdout_value = 0


if __name__ == '__main__':
    # func1()
    func2()
