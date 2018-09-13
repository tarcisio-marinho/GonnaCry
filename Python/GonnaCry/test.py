import os

import subprocess

if __name__=="__main__":

    # gnome = 'gnome-terminal --command ./bin/decryptor'
    # os.system(gnome)




    process = subprocess.Popen("pidof decryptor", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    output = process.stdout.read() + process.stderr.read()
    print(output)
    if(output):
        print("ALREADY RUNNING")
        exit(-1)
    
    gnome = 'gnome-terminal --command ./bin/decryptor'
    os.system(gnome)