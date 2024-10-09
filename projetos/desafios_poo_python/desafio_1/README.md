# DESCRIÇÃO
Você está desenvolvendo um sistema para gerenciar dados de vendas que serão posteriormente importados para o Power BI. Você tem a estrutura de duas classes, Venda e Relatorio, já definidas. Sua tarefa é implementar partes específicas do código dentro dessas classes.

## Criando Classes para Dados de Vendas
```bash
1) Classe Venda:

Já está definida e contém as informações sobre uma venda, como produto, quantidade e valor.

2) Classe Relatorio:

Você precisa implementar o método adicionar_venda, que deve verificar se o objeto passado é uma instância da classe Venda antes de adicioná-lo à lista de vendas.

Também, no método calcular_total_vendas, você deve calcular o total de vendas multiplicando a quantidade pelo valor de cada venda adicionada ao relatório.

3) Função main:
Você deverá implementar a lógica para exibir o total de vendas utilizando o método calcular_total_vendas da classe Relatorio.
```

```bash
Entrada
A entrada consiste em dados de vendas com as seguintes colunas:
Produto (string)
Quantidade (inteiro)
Valor (decimal)

Saída
A saída é o total de vendas calculado pela classe Relatorio.
```
## Exemplos de Uso

| Entrada                    | Saída                      |
|----------------------------|----------------------------|
| Notebook                   | Total de Vendas: 5500.0    |
| 3                          |                            |
| 1500.00                    |                            |
| Mouse                      |                            |
| 10                         |                            |
| 50.00                      |                            |
| Teclado                    |                            |
| 5                          |                            |
| 100.00                     |                            |
|                            |                            |

| Entrada                    | Saída                      |
|----------------------------|----------------------------|
| Monitor                    | Total de Vendas: 2020.0    |
| 2                          |                            |
| 800.00                     |                            |
| Webcam                     |                            |
| 1                          |                            |
| 120.00                     |                            |
| Fone de Ouvido             |                            |
| 4                          |                            |
| 75.00                      |                            |
|                            |                            |

| Entrada                    | Saída                      |
|----------------------------|----------------------------|
| Impressora                 | Total de Vendas: 930.0     |
| 1                          |                            |
| 350.00                     |                            |
| Cartucho                   |                            |
| 3                          |                            |
| 60.00                      |                            |
| Scanner                    |                            |
| 2                          |                            |
| 200.00                     |                            |

## Funcionamento do Código

- A classe `Venda` armazena informações sobre cada venda, incluindo produto, quantidade e valor.
- A classe `Relatorio` gerencia a lista de vendas e calcula o total de vendas.
- A função `main` coleta as informações do usuário e exibe o total de vendas calculado.

## Requisitos

- Python 3.x

## Como Executar

Para executar o programa, utilize o seguinte comando no terminal:

```bash
python desafio_1.py