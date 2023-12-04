import pandas as pd
import os

# Diretório onde os arquivos estão localizados
diretorio = './2023'  # Diretório atual, você pode ajustar para o seu diretório específico

# Listar todos os arquivos na pasta que são CSV
arquivos = [arq for arq in os.listdir(diretorio) if arq.endswith('.CSV')]

if not arquivos:
    print("Nenhum arquivo CSV encontrado no diretório.")
else:
    for arquivo in arquivos:
        try:
            # Carregar o arquivo CSV
            dados = pd.read_csv(os.path.join(diretorio, arquivo), sep=';', nrows=8, header=None, encoding='utf-8')

            # Transpor as primeiras 8 linhas
            dados_transpostos = dados.transpose()

            # Remover ':' do arquivo transposto
            dados_transpostos = dados_transpostos.applymap(lambda x: x.replace(':', '') if isinstance(x, str) else x)

            # Salvar os dados transpostos em um novo arquivo com ';' como separador
            dados_transpostos.to_csv(f'{os.path.splitext(arquivo)[0]}_primeiras_transpostas.csv', header=False, index=False, sep=';')

            # Remover as primeiras 8 linhas do arquivo original
            dados_restantes = pd.read_csv(os.path.join(diretorio, arquivo), sep=';', skiprows=8, encoding='utf-8')
            dados_restantes.to_csv(f'{os.path.splitext(arquivo)[0]}_restante.csv', sep=';', index=False)

        except Exception as e:
            print(f"Erro ao processar {arquivo}: {e}")

    print("Processo concluído.")