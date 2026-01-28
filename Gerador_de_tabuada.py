
N = int(input("Digite um numero de 0 a 10: "))
taboada = 0
contador = 0
    
while contador <=10:
    if N < 1 or N >10:
     N = int(input("valor invalido, informe um numero de 1 a 10: ")) 
  
else:
    taboada = N * contador
    print(f"{N} x {contador} = {taboada}")
    contador += 1