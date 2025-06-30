valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

valor_dolares = valor_reais / taxa_dolar
valor_euros = valor_reais / taxa_euro

print(f"Valor em reais: R$ {valor_reais:.2f}")
print(f"Taxa do dólar: R$ {taxa_dolar:.2f}")
print(f"Taxa do euro: R$ {taxa_euro:.2f}")
print(f"Valor em dólares: $ {valor_dolares:.2f}")
print(f"Valor em euros: € {valor_euros:.2f}")
