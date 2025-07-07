pares = 0
impares = 0
numeros_inseridos = []

print("Contador de Números Pares e Ímpares")
print("Digite números inteiros ou 'fim' para terminar:")

while True:
    entrada = input("Digite um número: ")
    
    if entrada.lower() == 'fim':
        break
    
    try:
        numero = int(entrada)
        numeros_inseridos.append(numero)
        
        if numero % 2 == 0:
            print(f"{numero} é par")
            pares += 1
        else:
            print(f"{numero} é ímpar")
            impares += 1
            
    except ValueError:
        print("Erro: Digite um número inteiro válido ou 'fim' para terminar!")

print(f"\nResumo:")
print(f"Total de números inseridos: {len(numeros_inseridos)}")
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")

if numeros_inseridos:
    print(f"Números inseridos: {numeros_inseridos}")
