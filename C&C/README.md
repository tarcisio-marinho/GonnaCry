# NESTE REPOSITÓRIO, CONTÉM O CODIGO DO SERVIDOR E SUAS CHAVES
    esta pasta deve ficar separado da maquina infectada, como em um cenário real.
    
    As chaves que eu utilizei aqui devem ser mudadas apenas 1 vez.
    
    Altere o código do servidor-> comente a linha da conexão: #conexao('localhost')
    
    Descomente a linha de gera_chaves()
    
    Gere apenas uma vez as chaves. 
    
    O usuario deve ter a chave pública, então copie o arquivo: CHAVE_PUBLICA_SERVIDOR.txt, e salve na pasta keys, dentro da pasta GonnaCry_1.0.
    
    Ficando assim: Ransomware/GonnaCry_1.0/keys/CHAVE_PUBLICA_SERVIDOR.txt

# Cuidados com a chave privada.
    manter o segredo da chave privada do servidor, é fundamental para o funcionamento do ransom.
    Caso a chave privada for vazada, todos os infectados terão como descriptografar seus arquivos. Ela é única possível de descriptografar tudo de todos.
