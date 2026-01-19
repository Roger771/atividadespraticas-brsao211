import pandas as pd

def processar_logs_treinamento(arquivo_log):
    try:
        leitor = pd.read_csv(arquivo_log)
        media = leitor['tempo_execucao'].std()
        desvio_padrao = leitor['tempo_execucao'].std()
        return f"Média: {media} Desvio Padrão: {desvio_padrao}"
    
    except FileNotFoundError:
        return "Arquivo não encontrado"
    


arquivo = input("Digite o nome do arquivo de log: ")
print (processar_logs_treinamento(arquivo))

        