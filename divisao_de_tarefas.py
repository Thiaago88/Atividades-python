conta = 150
divisao_exata = (conta % 3 == 0)

total = conta / 3 

print(f"Cada um vai pagar , R${total: .2f}")
print("A divisão e exata", divisao_exata)