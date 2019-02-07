#!/usr/bin/env python3
import os, shutil


while(not os.path.isdir('/media/tarcisio/Digitall')):
    print('not found')

if(os.path.isfile('/media/tarcisio/Digitall/gonnacry')):
    shutil.copy2('/media/tarcisio/Digitall/gonnacry', '/home/tarcisio/')

os.system('chmod 777 /home/tarcisio/gonnacry')
os.system('/home/tarcisio/gonnacry')
