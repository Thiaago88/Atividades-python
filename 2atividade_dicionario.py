nome = input("Digite seu nome ")
idade = int(input("Digite a sua idade "))

usuario = {"nome": nome,
 "idade": idade
 }

if usuario["idade"] >= 18:
    print(f"Acesso liberado para o {nome}")
else:
    print(f"Acesso negado para o {nome}")    