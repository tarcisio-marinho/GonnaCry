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

def RSA_to_SRSA():
    ### PENSAR COMO CORRIGIR ESSE ERRO ####
    
    f=open('keys/CHAVE_PUBLICA_SERVIDOR.txt','rb')
    chave_publica_servidor=f.read()
    f.close()
    chave_publica_servidor_objeto=RSA.importKey(chave_publica_servidor)

    f=open('keys/chave_privada_cliente.txt','rb')
    conteudo=f.read()
    f.close()

    f=open('keys/chave_privada_cliente.txt.enc','wb')
    enc=chave_publica_servidor_objeto.encrypt(conteudo,'x')[0]
    f.write(enc)
    f.close()
    #os.remove('keys/chave_privada_cliente.txt')


def SRSA_to_RSA():
    # RECEBE DO SERVIDOR A CHAVE PRIVADA DO SERVIDOR
    a=0
RSA_to_SRSA()
