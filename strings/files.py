#/usr/bin/python

if __name__ == '__main__':
	f = open('LinuxPamSag.txt','r')
	#print(f.read())
	#A more secure and error-tolerant way of openning a file :)	
	try:
		outF = open('outPutFile.txt', 'w')
		outF.write("this is a Text File\nTo test file creation\n")
	finally:
		outF.close()
	#the with statement, which lets you use context managers.
	#A context manager is simply an object with an __enter__() and __exit__().
	with open('writeable.txt','w') as f:
		f.write('This is a Writable File\nwhich was created by with statement\n')
	#the following shows f state and most importantely , it shows it is closed by
	#the context manager
	print(f)
