# GonnaCry Rasonware 

[![Travis branch](https://img.shields.io/travis/rust-lang/rust/master.svg)](https://github.com/tarcisio-marinho/GonnaCry)
[![Travis branch](https://img.shields.io/cran/l/devtools.svg)](https://github.com/tarcisio-marinho/GonnaCry/blob/master/LICENSE)
[![Travis branch](https://img.shields.io/badge/made%20with-%3C3-red.svg)](https://github.com/tarcisio-marinho/GonnaCry)
[![Travis branch](https://img.shields.io/github/stars/tarcisio-marinho/GonnaCry.svg)](https://github.com/tarcisio-marinho/GonnaCry/stargazers)
    
-------------

# Disclaimer
This repository is OpenSource, feel free to use, study and/or send pull request.
This Ransomware musn't be used to harm/threat/hurt other person's computer.
It's purpose is only to share knowledge and awareness about virus/Operating Sistems.

Knowledge is power!

[EN] GonnaCry is a linux Ransomware that encrypt all user files.
GonnaCry should not be used to harm people, it's just a academic ransomware made for learning and awareness about secutiry.
The program isn't complete nor all the funcionalities are working.

**Be aware running C/bin/GonnaCry or Python/GonnaCry/main.py in your computer, it may harm.**

# What's a Ransomware?
Ransomware is a computer virus that prevent's people of using the computer either cryptographing the files or blocking de screen to the user.

GonnaCry only cryptograph files.
If you want to run a test in your computer : https://github.com/tarcisio-marinho/Ransomware/blob/master/tests/README.md
This test only affect the files in the test directory.

~$ sudo pip install -r requeriments.txt

# Walkthrough



# Objectives:
- [x] Cryptograph all user's file with AES-256-CBC.
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
    - C -> C version of the GonnaCry Ransomware.
    - Python -> Python version of the GonnaCry Ransomware.
