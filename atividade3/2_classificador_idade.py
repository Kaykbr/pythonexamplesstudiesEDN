idade = int(input("Digite sua idade: "))

if idade >= 0 and idade <= 12:
    classificacao = "Criança"
elif idade >= 13 and idade <= 17:
    classificacao = "Adolescente"
elif idade >= 18 and idade <= 59:
    classificacao = "Adulto"
elif idade >= 60:
    classificacao = "Idoso"
else:
    classificacao = "Idade inválida"

print(f"Idade: {idade} anos")
print(f"Classificação: {classificacao}")
