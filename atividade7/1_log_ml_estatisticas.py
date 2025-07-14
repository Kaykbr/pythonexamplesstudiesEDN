import statistics

def extrair_tempos_do_arquivo(nome_arquivo):
    tempos = []
    with open(nome_arquivo, 'r', encoding='utf-8') as f:
        for linha in f:
            linha = linha.strip()
            if not linha:
                continue
            # Tenta extrair número da linha
            try:
                if 'Tempo:' in linha:
                    tempo = float(linha.split('Tempo:')[1].strip())
                else:
                    tempo = float(linha)
                tempos.append(tempo)
            except Exception:
                continue
    return tempos

arquivo = input('Digite o nome do arquivo de log: ')
tempos = extrair_tempos_do_arquivo(arquivo)

if tempos:
    media = statistics.mean(tempos)
    desvio = statistics.stdev(tempos) if len(tempos) > 1 else 0.0
    print(f'Média dos tempos: {media:.4f}')
    print(f'Desvio padrão: {desvio:.4f}')
else:
    print('Nenhum tempo encontrado no arquivo.')
