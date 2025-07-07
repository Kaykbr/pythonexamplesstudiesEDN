def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    return valor_conta * (porcentagem_gorjeta / 100)

valor_conta = float(input("Digite o valor total da conta: R$ "))
porcentagem_gorjeta = float(input("Digite a porcentagem da gorjeta: "))

gorjeta = calcular_gorjeta(valor_conta, porcentagem_gorjeta)
total_pagar = valor_conta + gorjeta

print(f"Valor da conta: R$ {valor_conta:.2f}")
print(f"Gorjeta ({porcentagem_gorjeta}%): R$ {gorjeta:.2f}")
print(f"Total a pagar: R$ {total_pagar:.2f}")
