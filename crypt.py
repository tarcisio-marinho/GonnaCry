from Crypto.Cipher import AES
from Crypto import Random



chave=RSA.generate(2048)
chave_privada=chave.exportKey('DER')
chave_publica=chave.publickey().exportKey('DER')
f=open('chave_privada.txt','wb')
f.write(chave_privada)
f.close()
#f=open('chave_publica.txt','wb')
#f.write(chave_publica)
#f.close()

obj_chave_publica=RSA.importKey(chave_publica)

arquivo='requeriments.txt'
novo_arquivo='requeriments.txt.encript'

# leu o arquivo
f=open(arquivo,'rb')
conteudo=f.read()
f.close()

# criou novo arquivo
f=open(novo_arquivo,'wb')
enc = obj_chave_publica.encrypt(conteudo,'x')[0]
f.write(enc)
f.close()
