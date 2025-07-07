notas = []

print("Sistema de Registro de Notas")
print("Digite as notas (0-10) ou 'fim' para terminar:")

while True:
    entrada = input("Digite uma nota: ")
    
    if entrada.lower() == 'fim':
        break
    
    try:
        nota = float(entrada)
        
        if 0 <= nota <= 10:
            notas.append(nota)
            print(f"Nota {nota} registrada com sucesso!")
        else:
            print("Erro: A nota deve estar entre 0 e 10!")
            
    except ValueError:
        print("Erro: Digite um número válido ou 'fim' para terminar!")

if notas:
    media = sum(notas) / len(notas)
    print(f"\nResumo da Turma:")
    print(f"Total de notas registradas: {len(notas)}")
    print(f"Notas: {notas}")
    print(f"Média da turma: {media:.2f}")
else:
    print("Nenhuma nota foi registrada.")
