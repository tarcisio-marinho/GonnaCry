from Crypto.PublicKey import RSA

readsize = 127
writesize = 128

private_key = RSA.generate(writesize*8)
public_key = private_key.publickey()

f = open('teste.txt','rb')
p = open('teste.txt.enc','wb')
while True:
	data = f.read(readsize)
	if not data:
		break
	enc_data = public_key.encrypt(data, 32)[0]

	p.write(chr(len(enc_data)))
	p.write(enc_data)
p.close()
f.close()

f = open('teste.txt.enc','rb')
p = open('teste.novo.txt','wb')
while True:
	length = f.read(1)
	if not length:
		break
	data = f.read(ord(length))

	dec_data = private_key.decrypt(data)
	p.write(dec_data[:readsize])
p.close()
f.close()
