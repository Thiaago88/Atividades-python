num1 = float(input("Digite o primeiro numero "))
num2 = float(input("Digite o segundo numero "))
op   = input("Escolha um operador +, -, *, / ")


if op == "+":
    resultado = num1 + num2

elif op == "-":
    resultado = num1 - num2

elif op == "*":
    resultado = num1 * num2

elif op == "/":
    if num2 == 0:
     print("Erro divisão por zero!")
     resultado = num1  / num2

else: 
  print("Operação invalida!")

print("resultado", resultado)   
