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
