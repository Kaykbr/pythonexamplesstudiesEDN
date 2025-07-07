from datetime import datetime

def calcular_idade_em_dias(ano_nascimento):
    ano_atual = datetime.now().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365
    return idade_dias

ano_nascimento = int(input("Digite o ano de nascimento: "))
idade_dias = calcular_idade_em_dias(ano_nascimento)

print(f"Você tem aproximadamente {idade_dias} dias de vida.")
