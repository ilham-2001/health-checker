#!/usr/bin/env python3

import psutil
import shutil
import socket

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100

    return free > 20

def check_cpu_usage():
    usage = psutil.cpu_percent(.1)
    return usage < 75

def check_no_network():
    try:
        socket.gethostbyname('www.google.com')
        return False
    except:
        return True


def main():
    print(check_cpu_usage())
    print(check_disk_usage('/'))
    
    if not check_disk_usage('/') or not check_cpu_usage():
        print('ERROR')
    else:
        print('Everthing is OK')

    print(check_no_network())


main()
