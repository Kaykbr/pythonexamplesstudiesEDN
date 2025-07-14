import json

# Escrever dados em JSON
nome = input('Nome: ')
idade = input('Idade: ')
cidade = input('Cidade: ')

pessoa = {'nome': nome, 'idade': idade, 'cidade': cidade}

with open('pessoa.json', 'w', encoding='utf-8') as f:
    json.dump(pessoa, f, ensure_ascii=False, indent=2)
print('Dados salvos em pessoa.json!')

# Ler dados do JSON
def ler_json():
    with open('pessoa.json', 'r', encoding='utf-8') as f:
        dados = json.load(f)
        print('Conteúdo do arquivo pessoa.json:')
        print(dados)

ler_json()
