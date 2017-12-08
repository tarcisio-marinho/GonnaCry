# GonnaCry Rasomware 
Original Repository of the GonnaCry Ransomware.

This project is OpenSource, feel free to use, study and/or send pull request.

GonnaCry is a linux Ransomware that encrypt all user files.

There is two versions of the Ransomware Code: C and Python.

Actually I'm working on the C code.

**How this ransomware work's**

https://0x00sec.org/t/how-ransomware-works-and-gonnacry-linux-ransomware/4594

[![Travis branch](https://img.shields.io/travis/rust-lang/rust/master.svg)](https://github.com/tarcisio-marinho/GonnaCry)
[![Travis branch](https://img.shields.io/cran/l/devtools.svg)](https://github.com/tarcisio-marinho/GonnaCry/blob/master/LICENSE)
[![Travis branch](https://img.shields.io/badge/made%20with-%3C3-red.svg)](https://github.com/tarcisio-marinho/GonnaCry)
[![Travis branch](https://img.shields.io/github/stars/tarcisio-marinho/GonnaCry.svg)](https://github.com/tarcisio-marinho/GonnaCry/stargazers)
    
-------------

# Disclaimer
This Ransomware musn't be used to harm/threat/hurt other person's computer.

It's purpose is only to share knowledge and awareness about Computer virus/Operating Sistems/Programming.

GonnaCry is a academic ransomware made for learning and awareness about secutiry.

The program isn't complete nor all the funcionalities are working.

Knowledge is power!


**Be aware running C/bin/GonnaCry or Python/GonnaCry/main.py in your computer, it may harm.**

-------------

# What's a Ransomware?
Ransomware is a computer virus that prevent's people of using the computer either cryptographing the files or blocking the screen to the user use.

It forces the victim to pay a ransom in order to get the files/computer back.

GonnaCry only cryptograph the user files.

-------------

# Walkthrough
The first step of the ransomware is to declare some enviroment/path variables, 
such as home, desktop, username, etc...

Then the find_files function will seach all the filetypes that matches with the extension
and append to the files List.

The encrypt_files function will walkthrough this List and generate randomly, unique Key and IV 
for each file. Then append the Key, IV and path to the new file inside a new List, Encrypted.

The encrypt function is called by encrypt_files, as he walkthrough the found files.

After encrypting, the file is shred(Filled with zeros) and deleted. This will protect against
recovery tools from getting the original file back.

The save_into_file_encrypted_list will get the Encrypted List, that contains the key, iv and path from each file
and save on the user's desktop as the file: enc_files.gc. This file will be used to decrypt the files.

All the memory allocated is released by functions such as destroy, and inside each function the strings allocated
are desalocated as well.

This make the ransomware to not consume much RAM memory.

-------------

# Objectives:
The general objective is to encrypt the files and get it back.

See each code version Features/Objectives:

**C**


https://github.com/tarcisio-marinho/GonnaCry/blob/master/C/README.md#features

**Python**


https://github.com/tarcisio-marinho/GonnaCry/blob/master/Python/README.md#objectives

-------------

# Sub-Dirs:
    - C -> C version of the GonnaCry Ransomware.
    - Python -> Python version of the GonnaCry Ransomware.
