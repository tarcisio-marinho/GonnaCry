# Python GonnaCry version

This directory contains the Python original code of the GonnaCry ransomware

**Be aware running GonnaCry/main.py GonnaCry/bin/gonnacry in your computer, it may harm.**

# How this version works:

https://medium.com/@tarcisiomarinho/ransomware-encryption-techniques-696531d07bb9



# Requeriments 

GonnaCry requires the pycrypto library and requests, installation below

    ~$ sudo pip install -r requeriments.txt

# Compiling the code

    ~$ pyinstaller -F --clean main.py -n gonnacry

    ~$ pyinstaller -F --clean decryptor.py -n decryptor


# Objectives:
- [x] encrypt all user files with AES-256-CBC.
- [x] Random AES key and IV for each file.
- [x] Works even if computer internet connection down.
- [x] Communication with the server to get Servers-private-key.
- [x] encrypt AES key with client-public-key RSA-2048.
- [x] encrypt client-private-key with RSA-2048 server-public-key.
- [x] Change computer wallpaper -> Gnome, LXDE, KDE, XFCE.
- [x] Decryptor communicating to server
- [x] python webserver
- [x] Daemon
- [ ] Program completed.
