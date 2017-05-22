from Crypto.PublicKey import RSA
file_enc='teste.txt.enc'
novo='teste.txt'
file_priv='chave_privada.txt'
f=open(file_priv,'rb')
chave_privada=f.read()
f.close()
f=open(file_enc,'rb')
dados=f.read()
f.close()
chave_privada_obj=RSA.importKey(chave_privada)
dados_dec=chave_privada_obj.decrypt(dados)
f=open(novo,'w')
f.write(dados_dec)
f.close()
