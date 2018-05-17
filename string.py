#!/usr/bin/python
import subprocess

if __name__ == '__main__':
	res = subprocess.Popen(['uname', '-sv'], stdout=subprocess.PIPE)
	uname = res.stdout.read().strip()
	print(uname)
	print('Linux' in uname)
	print('Darwin' not in uname)

