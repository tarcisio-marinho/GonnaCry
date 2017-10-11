# WaterRansomware

This is a water drinking awareness Ransomware
You should drink 1.5 - 2 galons of water every day!
Have you already drunk ?

# dependencies

     libssl-dev


# compiling yourself

    gcc main.c lib/func.c lib/struct.c  -o ransom -lcrypto

# features

  [x] Encrypt all files with AES-CBC 256.
  [x] Decrypt all files.
  [x] Save path, key and iv from each file on the desktop.
  [ ] Encrypt this file with RSA 1024 or 2048.
  [ ] Decrypt this file and read to get the path, key and iv from the file.
  [ ] Change wallpaper -> still figuring out how to salve the img on the code.
  [ ] 
