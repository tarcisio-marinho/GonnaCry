#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
from Crypto.PublicKey import RSA
import os
# CODIGO PARA CRIPTOGRAFAR A CHAVE PRIVADA DO CLIENTE COM A CHAVE PUBLICA DO SERVIDOR

def generate_data(length):
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join(random.SystemRandom().choice(chars) for _ in range(length))

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

def RSA_to_SRSA():
	# CRIPTOGRAFA A CHAVE PRIVADA DO CLIENTE COM A CHAVE PUBLICA DO SERVIDOR
	readsize = 127
	writesize = 128
	f = open('keys/chave_privada_cliente.txt','rb')
	p = open('keys/chave_privada_cliente.txt.enc','wb')
	g = open('keys/CHAVE_PUBLICA_SERVIDOR.txt','rb')
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
	shred('keys/chave_privada_cliente.txt',1)

def SRSA_to_RSA():
	# DESCRIPTOGRAFA A CHAVE PRIVADA DO CLIENTE COM A CHAVE PRIVADA DO SERVIDOR
	readsize = 127
	writesize = 128
	f = open('keys/chave_privada_cliente.txt.enc','rb')
	p = open('keys/chave_privada_cliente.txt','wb')
	g = open('keys/CHAVE_PRIVADA_SERVIDOR.txt','rb')
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
	os.remove('keys/chave_privada_cliente.txt.enc')
	os.remove('keys/CHAVE_PRIVADA_SERVIDOR.txt')
