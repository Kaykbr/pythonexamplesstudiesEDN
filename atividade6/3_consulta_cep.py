import requests

def consultar_cep(cep):
    try:
        cep_limpo = cep.replace("-", "").replace(".", "").replace(" ", "")
        
        if len(cep_limpo) != 8 or not cep_limpo.isdigit():
            print("CEP inválido! Digite um CEP com 8 dígitos.")
            return
        
        url = f"https://viacep.com.br/ws/{cep_limpo}/json/"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            
            if 'erro' in data:
                print("CEP não encontrado!")
            else:
                print("=== Informações do Endereço ===")
                print(f"CEP: {data['cep']}")
                print(f"Logradouro: {data['logradouro']}")
                print(f"Bairro: {data['bairro']}")
                print(f"Cidade: {data['localidade']}")
                print(f"Estado: {data['uf']}")
        else:
            print("Erro ao consultar CEP. Tente novamente.")
            
    except requests.exceptions.RequestException:
        print("Erro de conexão. Verifique sua internet.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

cep = input("Digite o CEP: ")
consultar_cep(cep)
