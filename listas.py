nomes = []
contador = 0

while contador < 5:
    nome = input("Digite um nome ")
    nomes.append(nome)
    contador += 1

print(nomes)
for nome in nomes:
    print(nome)
