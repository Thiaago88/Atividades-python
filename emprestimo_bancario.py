valor_emprestimo = float(input("Qual será o valor do emprestimo? "))
renda_mensal = float(input("Digite o valor mensal da sua renda." ))
parcelas = int(input("Digite a quantidade de parcelas desejada." ))

parcela_limite = renda_mensal * 0.30 
valor_parcela = valor_emprestimo / parcelas

if valor_parcela < parcela_limite:

    print("emprestimo aprovado!")
    print(f"valor do emprestimo: R$ {valor_emprestimo: .2f}")
    print(f"numero de parcelas: {parcelas}X")
    print(f"valor a ser pago: R${valor_parcela: .2f}")
else:
    print("emprestimo reprovado! R$ {parcela_limite: .2f} execede o limite de 30% da renda mensal")    