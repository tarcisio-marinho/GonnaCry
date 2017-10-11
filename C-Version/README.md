# C GannaCry version
     
     I want to try making the WannaCry in C ANSI, so I just started this C-Version repo.
     The python version of GonnaCry still works, but right now i'm focusing on this C version.
     No new updates in the python code will come until finished with the C code.
     
     
# dependencies

- Debian and derivates:

sudo apt-get install libssl-dev

- fedora:

sudo dnf install openssl-devel

# Compiling
     
     gcc main.c lib/func.c lib/struct.c  -o ransom -lcrypto 

# Features

  [x] Encrypt all files with AES-CBC 256.
  
  [ ] shred file before removing.
  
  [x] Decrypt all files.
  
  [x] Save path, key and iv from each file on the desktop.
  
  [ ] Encrypt this file with RSA 1024 or 2048.
  
  [ ] Decrypt this file and read to get the path, key and iv from the file.
  
  [ ] Change wallpaper -> still figuring out how to salve the img on the code.
  
  [ ] 
