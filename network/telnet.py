#!/usr/bin/env python3.6
import pexpect
import getpass

HOST = "172.19.150.208"
user = input("Enter your remote account: ")
password = getpass.getpass()

child = pexpect.spawn ('telnet '+HOST)
child.expect ('Username: ')
child.sendline (user)
child.expect ('Password: ')
child.sendline (password)
# If the hostname of the router is set to "deep"
# then the prompt now would be "deep>"
routerHostname = "deep" #example - can be different
child.expect (routerHostname+'>')
child.sendline ('enable')