valor = int(input("Quanto deseja sacar?"))

if  valor >= 100:
    ced100 = valor // 100
    valor = valor % 100
    print(f"100: {ced100}")
else:
    ced100 = 0

if  valor >= 50:
    ced50 = valor // 50
    valor = valor % 50
    print(f"50: {ced100}")
else:
    ced50 = 0

if   valor >= 20:
     ced20 = valor // 20
     valor = valor % 20
     print(f"20: {ced20}")
else:
    ced20 = 0

if  valor >= 10:
    ced10 = valor // 10
    valor = valor % 10
    print(f"10: {ced10}")
else:
    ced10 = 0

if valor >= 5:
    ced5 = valor // 5
    valor = valor % 5
    print(f"5: {ced5}")
else:
    ced5 = 0

if  valor >= 2:
    ced2 = valor // 2
    valor = valor % 2
    print(f"2: {ced2}")
else:
    ced2 = 0

if valor != 0:
    print("Não tem cedulas disponiveis no momento!")
else:
    if ced100 != 0:
        print(f"{ced100} cededulas de R$100,00")   
    if ced50 != 0:
        print(f"{ced50} cededulas de R$50,00")
    if ced20 != 0:
        print(f"{ced20} cededulas de R$20,00")
    if ced10 != 0:
        print(f"{ced10} cededulas de R$10,00")    
    if ced5 != 0:
        print(f"{ced5} cededulas de R$5,00")
    if ced2 != 0:
        print(f"{ced2} cededulas de R$2,00")