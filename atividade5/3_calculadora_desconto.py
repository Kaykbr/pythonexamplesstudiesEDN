preco_original = float(input("Digite o preço do produto: R$ "))
percentual_desconto = float(input("Digite o percentual de desconto: "))

valor_desconto = preco_original * (percentual_desconto / 100)
preco_final = preco_original - valor_desconto

print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto ({percentual_desconto}%): R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")
