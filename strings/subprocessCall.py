#!/usr/bin/python
import subprocess
if __name__ == '__main__':
	cmd='ps -ef|grep kernel'
	proc = subprocess.Popen(['ps','-ef'], stdout=subprocess.PIPE)
	proc1 = subprocess.Popen(['grep','kernel'], stdin=proc.stdout, stdout=subprocess.PIPE)
	value = proc1.communicate()[0]
	print(value)
	
