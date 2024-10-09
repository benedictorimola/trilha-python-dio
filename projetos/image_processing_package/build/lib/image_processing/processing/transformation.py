# transformation.py

import os
import cv2
import numpy as np

def adicionar_marca_dagua(imagem_path, marca_dagua_path, output_path):
    """Adiciona uma marca d'água a uma imagem e salva a nova imagem."""
    # Lê a imagem original e a marca d'água
    imagem = cv2.imread(imagem_path)
    marca_dagua = cv2.imread(marca_dagua_path, cv2.IMREAD_UNCHANGED)

    # Redimensiona a marca d'água
    largura, altura = imagem.shape[1], imagem.shape[0]
    nova_largura = int(largura * 0.3)
    nova_altura = int((nova_largura / marca_dagua.shape[1]) * marca_dagua.shape[0])
    marca_dagua = cv2.resize(marca_dagua, (nova_largura, nova_altura), interpolation=cv2.INTER_AREA)

    # Define a posição da marca d'água (canto inferior direito)
    posicao_x = largura - nova_largura - 10
    posicao_y = altura - nova_altura - 10

    # Cria uma máscara e um inverso da máscara
    if marca_dagua.shape[2] == 4:  # Se a marca d'água tem um canal alfa
        alpha_marca = marca_dagua[:, :, 3] / 255.0
        for c in range(0, 3):
            imagem[posicao_y:posicao_y + nova_altura, posicao_x:posicao_x + nova_largura, c] = (
                imagem[posicao_y:posicao_y + nova_altura, posicao_x:posicao_x + nova_largura, c] * (1 - alpha_marca) +
                marca_dagua[:, :, c] * alpha_marca
            )
    else:
        imagem[posicao_y:posicao_y + nova_altura, posicao_x:posicao_x + nova_largura] = marca_dagua

    # Salva a imagem resultante
    cv2.imwrite(output_path, imagem)

def processar_imagens(diretorio_entrada, marca_dagua_path, diretorio_saida):
    """Processa todas as imagens em um diretório, adicionando uma marca d'água."""
    os.makedirs(diretorio_saida, exist_ok=True)

    for arquivo in os.listdir(diretorio_entrada):
        if arquivo.lower().endswith(('.png', '.jpg', '.jpeg')):
            imagem_path = os.path.join(diretorio_entrada, arquivo)
            output_path = os.path.join(diretorio_saida, f'marcada_{arquivo}')
            adicionar_marca_dagua(imagem_path, marca_dagua_path, output_path)
            print(f'Marca d\'água adicionada a {arquivo}')
