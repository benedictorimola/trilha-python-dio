# CRIAÇÃO DE SISTEMA BANCÁRIO 

**Curso:** Bootcamp NTT DATA - Engenharia de Dados com Python<br>
**Seção:** Sintaxe básica com pyhton<br>
**Projeto:** Criando um sistema bancário com python<br>

### Disclaimer:
Este documento possui aas definições de todas as versões em ordem decrescente.

### Objetivo: <br>
Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.<br>
**Foi utilizada a versão python 3.12.5**

### DEFINIÇÃO DA VERSÃO 3:
#### A partir da versão 2, implemente as funcionalidades abaixo:
Permitir cadastramento de clientes pessoa física e pessoa jurídica<br>
Um cliente pode ter mais de uma conta<br>
A conta pode ser do tipo CC (Conta Corrente) ou P (Poupança)

**Importante:** este sistema será melhorado de forma contínua, objetivando a fatoração de código e implementação de novas funiocnalidades, como transferência entre C/C e poupança, e vice-versa; transferências entre contas e utilização de um banco de dados para armazenamento de dados.

### DEFINIÇÃO DA VERSÃO 2:
#### A partir da versão inicial, implemente as funcionalidades abaixo:

Criar as funcionalidades:<br>
Criação de cliente<br>
Criação de conta<br>

O desafio da versão 2 também solicitava o uso de uso de argumentos Keyword only and positional. <br> 
Para atende esta solicitação, apliquei o uso de "Keyword only and positional" na na funcionalidade depósito.<br>

#### Como implementei:
Criação de 3 menus:<br>
Menu SISTEMA BANCÁRIO, que direciona para o menu ADMINISTRATIVO ou CONTA CLIENTE.<br>
O menu ADMINISTRATIVO

Esta versão permite:<br>
O cadastramento de mais de um cliente.<br>
O cadastramento de mais de um conta.<br>
Uma conta só pode estar associada a um cliente.<br>
O extrato é capaz de gerar as inforamções de movimentções de uma conta, a  partir da informações bancárias informadas no MENU CONTA CLIENTE.<br>

#### Descrição dos Menus<br>

MENU SISTEMA BANCÁRIO<br>
[1] Administrativo<br>
[2] Conta Cliente<br>
[9] Encerrar<br>

MENU ADMINISTRATIVO<br>
[1] Nova conta<br>
[2] Novo cliente<br>
[3] Listar Contas<br>
[4] Retorna menu anterior<br>
[9] Encerrar<br>

MENU CONTA CLIENTE<br>
[1] Saque<br>
[2] Depósito<br>
[3] Extrato<br>
[4] Retorna menu anterior<br>
[9] Encerrar<br>

#### Pequenas validações<br>
Algumas validações foram implementadas, como uma evolução do desafio, com objetivo de aprimorar e treinar a lógica e uso da linguagem python, com opor exemplo:<br>
- Tamnhos mínimo e máxio das informações solicitadas, com opor exemplo cpf e  nome<br>
- Formato de entrada da data de nascimento

### DEFINIÇÃO DA VERSÃO INICIAL:

### 1) Operação de saque<br>
O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

### 2) Operação de depósito<br>
Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.


### 3) Operação de extrato
Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.
Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:
1500.45 = R$ 1500.45
