numero = int(input("Digite um numero inteiro: "))
lista1 = []
lista2 = []
lista3 = []
lista4 = []
numero = 1

while contador < 1:
    if numero < 0 or numero > 25:
        print("Este numero não pertence a esta lista!")
    else:
        lista1.append(numero)
        contador += 1     

print(lista1)
   

