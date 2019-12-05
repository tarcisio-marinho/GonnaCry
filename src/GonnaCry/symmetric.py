import base64
import hashlib

import generate_keys

from Crypto import Random
from Crypto.Cipher import AES
# import generate_keys

class AESCipher(object):

    def __init__(self, key): 
        self.bs = 32
        self.key = hashlib.sha256(key).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc, decryption_key=None):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        if(decryption_key):
            self.key = hashlib.sha256(decryption_key).digest()
            
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:]))

    def _pad(self, s):
        s = s.decode('utf-8')
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

if __name__ == "__main__":
    key = generate_keys.generate_key(32, True)
    cipher_obj = AESCipher(key)
    print("chave: {}".format(key))
    enc = cipher_obj.encrypt("TESTE CRYPTO")
    print(enc)

    back = cipher_obj.decrypt(enc, key)

    print(back)