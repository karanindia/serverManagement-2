#!/usr/bin/python
import subprocess
import os

if __name__ == '__main__':
	res = subprocess.Popen(['uname', '-sv'], stdout=subprocess.PIPE)
	uname = res.stdout.read().strip()
	print(uname)
	print('Linux' in uname)
	print('Darwin' not in uname)
	print(uname.index('Linux'))
	print(uname.find('Unix'))
	print(type(uname))
	print(uname[1:])
	print(' '.join(uname.split(' ')[1:]))
	some_list = range(10)
	print(','.join([str(i) for i in some_list]))
	directory = subprocess.Popen(['pwd'], stdout=subprocess.PIPE)
	folder = directory.stdout.read().strip().split('/')
	print(''.join(folder[len(folder)-1:]))
	textFilesProc = subprocess.Popen(['find', '/', '-name', '*.txt'], stdout=subprocess.PIPE)
	textFiles = textFilesProc.stdout.read().strip().split('\n')
	print(len(textFiles))
	subprocess.call(['cat', textFiles[500]], shell=False)
