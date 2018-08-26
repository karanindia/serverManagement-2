#!/usr/bin/env python3.6
import sys, os, string, subprocess

#Getting search pattern from user and assigning it to a list
if __name__ == '__main__':
        try:
                #run a 'find' command and assign results to a variable
                pattern = input("Enter the file pattern to search for:")
                commandString = "find " + pattern
                commandOutput = subprocess.getoutput(commandString)
                findResults = commandOutput.split('\n')
                print ("Files:")
                print ("================================")
                for file in findResults:
                        print(file)
        except:
                print ("There was a problem")
