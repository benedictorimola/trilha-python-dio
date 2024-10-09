# DESCRIÇÃO
Você está desenvolvendo um sistema para organizar vendas por categorias antes de gerar um relatório. O objetivo é criar uma classe Categoria que gerencie as vendas associadas a uma determinada categoria e calcule o total de vendas dessa categoria.

## Agrupamento de Vendas por Categoria
```bash
Tarefas:

Método adicionar_venda: Na classe Categoria, crie um método chamado adicionar_venda que adiciona um objeto Venda à lista de vendas da categoria.

Método total_vendas: Na classe Categoria, crie um método chamado total_vendas que calcula e retorna o total das vendas (soma do valor de todas as vendas) para essa categoria.

Na função main:

Entrada de Dados:
Leia o nome das categorias e, para cada categoria, leia as vendas associadas.
Implementação: Adicione cada venda à categoria correspondente usando o método adicionar_venda.

Exibição dos Resultados:
Exiba o total de vendas para cada categoria.
Implementação: Utilize o método total_vendas para calcular e exibir o total das vendas.
```

```bash
Entrada
A entrada consiste em:

Nome da Categoria (string)

Lista de Vendas (com as colunas Produto, Quantidade, Valor)
Atenção:
O valor será o TOTAL GERAL de todos os produtos. Dessa forma:

Eletrônicos

- Celular, 5, 1000 - Produto Celular, temos 5 unidade e o valor total é 1000;
- Fone de Ouvido, 10, 500 - Produto Fone de Ouvido, temos 10 unidades e o valor total é 500;

Saída
A saída é o total de vendas por categoria.
```


# Sistema de Gerenciamento de Vendas

Este sistema é projetado para gerenciar dados de vendas em diferentes categorias e calcular o total de vendas para cada categoria.

## Como Usar

1. Execute o programa.
2. Insira as informações de vendas conforme solicitado.
3. O sistema calculará e exibirá o total de vendas por categoria.

## Exemplos de Uso

| Entrada                                | Saída                       |
|----------------------------------------|-----------------------------|
| Eletrônicos                            | Vendas em Eletrônicos: 1500.0 |
| Celular, 5, 1000                       |                             |
| Fone de Ouvido, 10, 500                |                             |

| Entrada                                | Saída                       |
|----------------------------------------|-----------------------------|
| Móveis                                 | Vendas em Móveis: 1200.0     |
| Mesa, 2, 800                           |                             |
| Cadeira, 4, 400                        |                             |

| Entrada                                | Saída                       |
|----------------------------------------|-----------------------------|
| Alimentos                              | Vendas em Alimentos: 340.0    |
| Arroz, 10, 200                         |                             |
| Feijão, 7, 140                         |                             |
| Jardinagem                             | Vendas em Jardinagem: 160.0   |
| Planta, 2, 60                          |                             |
| Ferramentas, 1, 100                    |                             |

| Entrada                                | Saída                       |
|----------------------------------------|-----------------------------|
| Livros                                 | Vendas em Livros: 170.0      |
| Aventuras no Tempo, 1, 80              |                             |
| Mistérios do Oceano, 2, 90             |                             |
| Esportes                               | Vendas em Esportes: 330.0     |
| Tênis, 7, 210                          |                             |
| Bola, 3, 120                           |                             |

## Funcionamento do Código

- O sistema categoriza as vendas em diferentes áreas, como eletrônicos, móveis, alimentos, jardinagem, livros e esportes.
- Cada venda inclui informações sobre o produto, quantidade e valor.
- O total de vendas para cada categoria é calculado e exibido.

## Requisitos

- Python 3.x

## Como Executar

Para executar o programa, utilize o seguinte comando no terminal:

```bash
python desafio_2.py
