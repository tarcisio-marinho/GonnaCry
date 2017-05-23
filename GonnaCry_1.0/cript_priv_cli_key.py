from Crypto.PublicKey import RSA
import os
f=open('chave_privada.txt','rb')
k=open('chave_publica.txt','rb')

chave_privada=f.read()
chave_publica=k.read()
f.close()
k.close()

chave_privada_objeto=RSA.importKey(chave_privada)
chave_publica_objeto=RSA.importKey(chave_publica)

original='teste.txt'
novo='teste.txt.enc'
#f=open(original,'rb')
#conteudo=f.read()
#f.close()

#f=open(novo,'wb')
#enc=chave_publica_objeto.encrypt(conteudo,'x')[0]
#f.write(enc)
#f.close()
#os.remove(original)

f=open(novo,'rb')
conteudo=f.read()
f.close()

dados_dec=chave_privada_objeto.decrypt(conteudo)
f=open(original,'w')
f.write(dados_dec)
f.close()
os.remove(novo)
