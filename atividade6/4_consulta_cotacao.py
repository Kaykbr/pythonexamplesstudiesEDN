import requests
from datetime import datetime

def consultar_cotacao(codigo_moeda):
    try:
        url = f"https://economia.awesomeapi.com.br/last/{codigo_moeda.upper()}-BRL"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            chave = f"{codigo_moeda.upper()}BRL"
            
            if chave in data:
                cotacao = data[chave]
                
                print(f"=== Cotação {codigo_moeda.upper()}/BRL ===")
                print(f"Valor atual: R$ {float(cotacao['bid']):.4f}")
                print(f"Valor máximo: R$ {float(cotacao['high']):.4f}")
                print(f"Valor mínimo: R$ {float(cotacao['low']):.4f}")
                
                timestamp = int(cotacao['timestamp'])
                data_atualizacao = datetime.fromtimestamp(timestamp)
                print(f"Última atualização: {data_atualizacao.strftime('%d/%m/%Y às %H:%M:%S')}")
            else:
                print("Moeda não encontrada! Verifique o código da moeda.")
        else:
            print("Erro ao consultar cotação. Tente novamente.")
            
    except requests.exceptions.RequestException:
        print("Erro de conexão. Verifique sua internet.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

print("Moedas disponíveis: USD, EUR, GBP, JPY, CAD, AUD, etc.")
codigo_moeda = input("Digite o código da moeda: ")
consultar_cotacao(codigo_moeda)
