#!/usr/bin/env python3.6

if __name__ == '__main__':
    #filePath = '/etc/sysconfig/network-scripts/'
    filePath = '/home/hossein/myScripts/'
    inputChoice = input('Which One Will You Do, Copy Template Config(1) or make new Config(2)?: ')
    if inputChoice == '1':
        with open(filePath + 'ifcfg-eth0', 'w') as ifFile:
            with open('ifcfg-eth0', 'r') as sourceFile:
                for i in sourceFile.readlines():
                    ifFile.write(i)
    elif inputChoice == '2':
        ifname = input('Please Enter Interface Name:')
        ipaddr = input('Please Enter IP Address:')
        netmask = input('Please Enter Net Mask:')
        gateway = input('Please Enter Gateway:')
        fileName = 'ifcfg-' + ifname
        try:
            with open(filePath + fileName, 'w') as ifFile:
                ifFile.write('DEVICE=' + ifname + '\n' +
                             'BOOTPROTO=static\n' + 'IPADDR=' + ipaddr +
                             '\n' + 'NETMASK=' + netmask + '\n' +
                             'GATEWAY=' + gateway + '\n' +
                            'ONBOOT=yes\n' + 'TYPE=Ethernet\n')
        except:
            print('No Such File Or Directory!')
    else:
        print('Unhandled Input')