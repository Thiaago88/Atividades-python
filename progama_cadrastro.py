nome = input("Nome: ")
while len(nome) <= 4:
    nome = input("Nome invalido, Digite o nome novamente: ")

idade = input("Idade: ")
while idade < 1 or idade > 27:
    idade = input("Idade invalida, Digite a idade novamente: ")

salario = input("Salario: ")
while salario >= 0 :
    salario = input("Salario invalido, Digite o salario novamente: ")


sexo = input("Sexo: ")
while sexo != "f" and sexo != "m":
    sexo = input("Salario invalido, Digite o salario novamente: ")

estado_civil = input("Estado civil: ")
while estado_civil != "solteiro" and estado_civil != "casado" and estado_civil != "viuvo" and  estado_civil  != "divorciado":
    estado_civil = input("Estado civil invalido, Digite novamente o estado civil: ")