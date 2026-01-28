usuario = ""
senha = ""

while usuario == senha:
    usuario = input("Digite o nome do usuario  ")
    senha = input("Digite uma senha ")
    if usuario == senha:
     print("Erro, a senha e usuario não podem ser iguais")

print("Cadastro realizado com sucesso!")



