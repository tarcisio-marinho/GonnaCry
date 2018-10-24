# THIS VERSION IS OUTDATED, GO CHECK PYTHON VERSION

# C GonnaCry version
This directory contains the C code of the GonnaCry Ransomware

**Be aware running bin/GonnaCry in your computer, it may harm.**

# Features
- [x] Encrypt all user files with AES-CBC 256.
  
- [x] Encrypt HD/pendrive on the victim machine.

- [x] Shred file before removing (Zeroing).
  
- [x] Decrypt all files.
  
- [x] Generate unique Key and IV for each file.

- [x] Save path, key and iv from each file on the desktop (recover file).
  
- [ ] Communicate with the server to exchange private key.

- [ ] Encrypt recover file with RSA 1024 or 2048.
  
- [ ] Decrypt recover file and read to get the path, key and iv from the file.
  
- [ ] Change wallpaper -> still figuring out how to save the img on the code.


# Dependencies
GonnaCry requires openssl Library, instalation below

- Debian and derivates:

     sudo apt-get install libssl-dev

- fedora:

     sudo dnf install openssl-devel

# Compiling
     
     ~$ cd GonnaCry/C
     ~$ make
     
     or 
     
     ~$ gcc main.c lib/func.c lib/struct.c lib/crypto.c -o bin/GonnaCry -lcrypto 
     
# Deleting

    ~$ make clean

