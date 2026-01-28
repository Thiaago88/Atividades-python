notas = []
quantidade = int(input("Quantas notas deseja informar?: "))
contador = 0

while contador < quantidade:
    nota = float(input("Digite uma nota: "))

    if nota < 0 or nota > 10:
        print("Valor inválido! Digite um número de 0 a 10.")
    else:
        notas.append(nota)
        contador += 1  

media = sum(notas) / quantidade

print("Quantidade de notas:", quantidade)
print(f"Média de todas as notas: {media:.2f}")
