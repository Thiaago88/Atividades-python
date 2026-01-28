N = int(input("Informe a quantidade de termos que deseja ver na serie fibonacci: "))
termo1 = 0
termo2 = 1
proximo_termo = 0
 
for i in range(1, N+1):
    print(termo1)
    proximo_termo = termo1 + termo2
    termo1 = termo2
    termo2 = proximo_termo