# NESTE REPOSITÓRIO, CONTÉM O CODIGO DO SERVIDOR E SUAS CHAVES
    esta pasta deve ficar separado da maquina infectada, em um cenário real.
    As chaves que eu utilizei aqui, foram geradas pelo meu algoritmo RSA, se quiser saber como foram criadas: https://medium.com/@tarcisiomarinho/algoritmo-de-criptografia-assim%C3%A9trica-rsa-c6254a3c7042
    se quiser ver o código que foi usado para gera-las: https://github.com/tarcisio-marinho/SSH/tree/master/RSA

# Cuidados com a chave privada.
    manter o segredo da chave privada do servidor, é fundamental para o funcionamento do ransom.
    Caso a chave privada for vazada, todos os infectados terão como descriptografar seus arquivos. Ela é única possível de descriptografar tudo de todos.
