import csv

with open('pessoas.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Nome', 'Idade', 'Cidade'])
    while True:
        nome = input('Nome (ou "fim" para sair): ')
        if nome.lower() == 'fim':
            break
        idade = input('Idade: ')
        cidade = input('Cidade: ')
        writer.writerow([nome, idade, cidade])
print('Arquivo pessoas.csv criado com sucesso!')
