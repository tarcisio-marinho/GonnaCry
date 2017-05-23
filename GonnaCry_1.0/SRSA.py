from Crypto.PublicKey import RSA
# CODIGO PARA CRIPTOGRAFAR A CHAVE PRIVADA DO CLIENTE COM A CHAVE PUBLICA DO SERVIDOR

def RSA_TO_SRSA():
	# CRIPTOGRAFA A CHAVE PRIVADA DO CLIENTE COM A CHAVE PUBLICA DO SERVIDOR
	readsize = 127
	writesize = 128
	f=open('chave_privada_cliente.txt','rb')
	p=open('chave_privada_cliente.txt.enc','wb')
	g=open('CHAVE_PUBLICA_SERVIDOR.txt','rb')
	public_key=g.read()

	while True:
		data = f.read(readsize)
		if not data:
			break
		enc_data = public_key.encrypt(data, 32)[0]

		p.write(chr(len(enc_data)))
		p.write(enc_data)
	p.close()
	f.close()
	g.close()

def SRSA_to_RSA():
	# DESCRIPTOGRAFA A CHAVE PRIVADA DO CLIENTE COM A CHAVE PRIVADA DO SERVIDOR
	readsize = 127
	writesize = 128
	f=open('chave_privada_cliente.txt.enc','rb')
	p=open('chave_privada_cliente.txt','wb')
	g=open('CHAVE_PRIVADA_SERVIDOR.txt','rb')
	private_key=g.read()

	while True:
		length = f.read(1)
		if not length:
			break
		data = f.read(ord(length))

		dec_data = private_key.decrypt(data)
		p.write(dec_data[:readsize])
	p.close()
	f.close()
	g.close()
