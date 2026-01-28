salario = float(input("Salario atual " ))


if salario <= 279:
    percentual = 20
elif salario <= 280 and salario < 700:
    percentual =  15
elif salario <= 700 and salario < 1500:
    percentual = 10
else:
    percentual = 5

aumento = salario * (percentual / 100)
novo_salario = salario + aumento


print(f"O salario antes do reajuste: {salario:.2f}")
print(f"O percentual de aumento aplicado: {percentual:.2f}%")
print(f"O valor do aumento R${aumento:.2f}")
print(f"O novo salario, após o aumento R${novo_salario:.2f}" )