
from hashlib import md5
from Crypto.Cipher import AES
from Crypto import Random

def derive_key_and_iv(password, salt, key_length, iv_length):
    d = d_i = ''
    while len(d) < key_length + iv_length:
        d_i = md5(d_i + password + salt).digest()
        d += d_i
    return d[:key_length], d[key_length:key_length+iv_length]

def encrypt(in_file, out_file, password, key_length=32):
    bs = AES.block_size # 16 -> int
    salt = Random.new().read(bs - len('Salted__')) # '\xabs-\xea\x98\x13`\xf2' -> string
    key, iv = derive_key_and_iv(password, salt, key_length, bs)

    # key = '\x96\xc2\xce\xd9Z\x0b\xe8\xecA\x9bO\x97~\x80\x0b\xca6\xd2\x10\x93\xf8W\x1e\x82\x10\x1eB\xe49\xe6\xe2('
    # iv = '\xbd\xbd\xd2\xdcX3j$F\xc4\xf8\x07v\x8c\xf8\x08'

    cipher = AES.new(key, AES.MODE_CBC, iv)
    # cipher = <Crypto.Cipher.AES.AESCipher instance at 0x7f13dbe818c0>
    out_file.write('Salted__' + salt)
    finished = False
    while not finished:
        chunk = in_file.read(1024 * bs)
        if len(chunk) == 0 or len(chunk) % bs != 0:
            padding_length = (bs - len(chunk) % bs) or bs
            chunk += padding_length * chr(padding_length)
            finished = True
        out_file.write(cipher.encrypt(chunk))

def decrypt(in_file, out_file, password, key_length=32):
    bs = AES.block_size
    salt = in_file.read(bs)[len('Salted__'):]
    key, iv = derive_key_and_iv(password, salt, key_length, bs)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    next_chunk = ''
    finished = False
    while not finished:
        chunk, next_chunk = next_chunk, cipher.decrypt(in_file.read(1024 * bs))
        if len(next_chunk) == 0:
            padding_length = ord(chunk[-1])
            chunk = chunk[:-padding_length]
            finished = True
        out_file.write(chunk)

import random, os, string

# A quick and dirty example to shred a single file in the current directory. | http://ubuntuforums.org/showthread.php?t=2299355
def generate_data(length):

    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join(random.SystemRandom().choice(chars) for _ in range(length))

## problem with script is memory error on large files :(

def shred(file_name,  passes):
    try:
        if not os.path.isfile(file_name):
            print(file_name + " is not a file.")
            return False

        ld = os.path.getsize(file_name)
        fh = open(file_name,  "w")
        for _ in range(int(passes)):
            data = generate_data(ld)
            fh.write(data)
            fh.seek(0,  0)

        fh.close()
        os.remove(file_name)
        return True

    except:
        return False
