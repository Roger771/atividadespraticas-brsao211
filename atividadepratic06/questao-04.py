import requests

def consultar_contacao(moeda):
    url = f"https://economia.awsomeapi.com.br/last/{moeda}BL"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()[f"{moeda.upper()}BRL"]

        cotacao = float(dados["bid"])
        alta = float(dados["high"])
        baixa = float(dados["low"]) 
        data = dados["create_date"]

        return f"Cotação: R${cotacao:.2f}\nAlta: R${alta:.2f}\mBaixa: R${baixa:.2f}\n Date: {date}"
    
    except requests.RequestException as e:
        return f"Erro ao consultar contação: {e}"
    

moeda = input("Digite a moeda (ex: USD, EUR, BTC, GBP): ")
resultado = consultar_contacao(moeda)
print(resultado)
    