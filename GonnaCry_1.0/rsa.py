from Crypto.PublicKey import RSA
import os
def AES_to_RSA():
    chave = RSA.generate(2048)
    chave_privada=chave.exportKey('DER')
    chave_publica=chave.publickey().exportKey('DER')
    f=open('keys/chave_privada_cliente.txt','wb')
    f.write(chave_privada)
    f.close()
    chave_publica_objeto=RSA.importKey(chave_publica)
    original='keys/AES.txt'
    novo='keys/AES.txt.enc'
    f=open(original,'rb')
    conteudo=f.read()
    f.close()
    f=open(novo,'wb')
    enc=chave_publica_objeto.encrypt(conteudo,'x')[0]
    f.write(enc)
    f.close()
    os.remove(original)
