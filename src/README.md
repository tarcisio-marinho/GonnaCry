# Python GonnaCry version

This directory contains the Python original code of the GonnaCry ransomware

**Be aware running GonnaCry/main.py GonnaCry/bin/gonnacry in your computer, it may harm.**

# How this version works:

https://medium.com/@tarcisiomarinho/ransomware-encryption-techniques-696531d07bb9

# Work flow

Gonnacry encrypt all files and call Daemon

Daemon encrypt new files, calls decryptor and change wallpaper

Decryptor try to communicate to server to send the Client private key wich is encrypted.

# Requeriments 

GonnaCry requires the pycrypto library and requests, installation below

    ~$ sudo pip install -r requeriments.txt

# Compiling the code

    ~$ pyinstaller -F --clean main.py -n gonnacry

    ~$ pyinstaller -F --clean decryptor.py -n decryptor


# Objectives:
- [x] encrypt all user files with AES-256-CBC.
- [x] Random AES key and IV for each file.
- [x] Works even without internet connection.
- [x] Communication with the server to decrypt Client-private-key.
- [x] encrypt AES key with client-public-key RSA-2048.
- [x] encrypt client-private-key with RSA-2048 server-public-key.
- [x] Change computer wallpaper -> Gnome, LXDE, KDE, XFCE.
- [x] Decryptor that communicate to server to send keys.
- [x] python webserver
- [x] Daemon
- [ ] Dropper

# GonnaCry src files

| File          | description   |
| ------------- |:-------------:|
| main.py      | GonnaCry start file|
| daemon.py     | dropped by main.py and run |
| dropper.py    | drop the malware on the computer |
| decryptor.py  | communicate with the server, decrypt keys and files|
| symmetric.py      |AES encryption|
| asymmetric.py | RSA encryption |
| generate_keys.py | Generate random AES keys|
| persistence.py | Persistence routines for linux OS|
| get_files.py | Find files to be encrypted|
| environment.py| environment variables|
| variables.py | Images and malware binaries|
| utils.py | Utilities routines|
