import os

# Lista dos códigos a serem mantidos
codigos_validos = {'A657', 'A617', 'A615', 'A631', 'A614', 'A632', 'A622', 'A613', 'A616', 'A633', 'A634', 'A612'}

# Diretório onde os arquivos estão localizados
diretorio = './2023'  # Diretório atual, você pode ajustar para o seu diretório específico

# Listar todos os arquivos na pasta
arquivos = [arq for arq in os.listdir(diretorio)]

for arquivo in arquivos:
    codigo_encontrado = False
    for codigo in codigos_validos:
        if codigo in arquivo:
            codigo_encontrado = True
            break
    
    if not codigo_encontrado:
        # Se nenhum dos códigos válidos estiver no nome do arquivo, exclua o arquivo
        os.remove(os.path.join(diretorio, arquivo))
        print(f"Arquivo {arquivo} removido.")

print("Processo concluído.")
