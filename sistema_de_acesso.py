senha_inserida = "abcd1234"
senha_correta = "abcd1234"
usuario_bloqueado = False

acesso = senha_inserida == senha_correta and not usuario_bloqueado

mensagem = "Acesso liberado!"
print(mensagem)