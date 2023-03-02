#!/usr/bin/env python3

import psutil
import shutil

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100

    return free > 20

def check_cpu_usage():
    usage = psutil.cpu_percent(.1)
    return usage < 75

if not check_disk_usage('/') or not check_cpu_usage():
    print('ERROR')
else:
    print('Everthing is OK')



def main():
    pass

main()
