# Python GonnaCry version
This directory contains the Python original code of the GonnaCry ransomware

**Be aware running GonnaCry/main.py in your computer, it may harm.**

If you want to run a test in your computer : https://github.com/tarcisio-marinho/GonnaCry/blob/master/Python/tests/README.md
This test only affect the files in the test directory.


# Requeriments 
GonnaCry requires the pycrypto library, installation below

    ~$ sudo pip install -r requeriments.txt

# Objectives:
- [x] Cryptograph all user files with AES-256-CBC.
- [x] Cryptograph other devices conected to the machine such as: pendrives/ External HD's.
- [x] Random AES key seed for each new infection.
- [x] Works even if computer internet connection down.
- [x] Communication with the server to get Servers-private-key.
- [x] Cryptograph AES key with client-public-key RSA-1024.
- [x] Cryptograph client-private-key with RSA-1024 server-public-key.
- [x] Change computer wallpaper.
- [x] Still work's if victim is offline.
- [ ] Decryptor GUI.
- [ ] Daemon waiting to new files/HD's to be cryptographed // Decryptor program.
- [ ] Program completed.

# Sub-Dirs:
    - C&C -> Server side application to send server-private-key (NOT WORKING)/(ACEPPTING PULL REQUESTS).
    - Decryptor -> Client side Decryptor app to decrypt files(INCOMPLETE)
    - GonnaCry -> Ransomware crypto code (WORKING BUT COMMENTED SOME PARTS)
    - tests -> directory to test the ransomware (TEST ZONE)

# Testing:
- doesnt affect your computer 

    cd /tests
    python criptografa.py
    python descriptografa.py
