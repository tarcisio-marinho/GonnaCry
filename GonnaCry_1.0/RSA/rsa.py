from Crypto.PublicKey import RSA
chave = RSA.generate(2048)
chave_privada=chave.exportKey('DER')
chave_publica=chave.publickey().exportKey('DER')
f=open('chave_privada.txt','wb')
f.write(chave_privada)
f.close()
chave_publica_objeto=RSA.importKey(chave_publica)
original='teste.txt'
novo='teste.txt.enc'
f=open(original,'rb')
dados=f.read()
f.close()
f=open(novo,'wb')
enc=chave_publica_objeto.encrypt(dados,'x')[0]
f.write(enc)
f.close()
