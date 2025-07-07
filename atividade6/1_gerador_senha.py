import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + "!@#$%&*()_+-=[]{}|;:,.<>?"
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

tamanho_senha = int(input("Digite o número de caracteres da senha: "))

if tamanho_senha <= 0:
    print("O tamanho da senha deve ser maior que zero!")
else:
    senha_gerada = gerar_senha(tamanho_senha)
    print(f"Senha gerada: {senha_gerada}")
