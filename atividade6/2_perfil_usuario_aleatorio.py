import requests
import json

def gerar_perfil_usuario():
    try:
        url = "https://randomuser.me/api/"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            usuario = data['results'][0]
            
            nome = f"{usuario['name']['first']} {usuario['name']['last']}"
            email = usuario['email']
            pais = usuario['location']['country']
            
            print("=== Perfil de Usuário Aleatório ===")
            print(f"Nome: {nome}")
            print(f"Email: {email}")
            print(f"País: {pais}")
            
        else:
            print("Erro ao acessar a API. Tente novamente.")
            
    except requests.exceptions.RequestException:
        print("Erro de conexão. Verifique sua internet.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

gerar_perfil_usuario()
