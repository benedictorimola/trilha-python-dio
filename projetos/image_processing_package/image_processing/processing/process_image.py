# main.py

from transformation import processar_imagens

# Configurações
diretorio_entrada = 'caminho/para/diretorio/entrada'  # Substitua pelo seu diretório de entrada
marca_dagua_path = 'marca_dagua.png'                   # Caminho da imagem da marca d'água
diretorio_saida = 'caminho/para/diretorio/saida'       # Substitua pelo seu diretório de saída

# Processa as imagens
processar_imagens(diretorio_entrada, marca_dagua_path, diretorio_saida)
