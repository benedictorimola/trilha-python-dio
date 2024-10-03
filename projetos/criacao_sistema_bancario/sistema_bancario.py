# VERSÃO 1
import time
mensagem_comprovante = "===> Aguarde a impressão do comprovante de depósito\n"
mensagem_operação = "===> Efetuando operação.  Aguarde."
LIMITE_SAQUES = 3

class ContaBancaria:
    def __init__(self):
        self.saldo = 0.0
        self.extrato = []
        self.saques_realizados = 0

    def depositar(self, valor_deposito):
        if valor_deposito > 0:
            self.saldo += valor_deposito
            self.extrato.append(f'Depósito: R$ {valor_deposito:.2f}')
            print(mensagem_operação)
            time.sleep(2)
            print(f'===> Depósito no valor de R$ {valor_deposito:.2f} efetuado com sucesso.')
            time.sleep(2)
            print(mensagem_comprovante)
        else:
            print('===>Valor de depósito deve ser maior que zero.')

    def sacar(self, valor_saque):
        if self.saques_realizados >= LIMITE_SAQUES:
            print('===> Limite de saques diários atingido para a data de hoje.')
        elif valor_saque > 500:
            print('===> O valor do saque não pode ser maior que R$ 500,00.')
        elif valor_saque > self.saldo:
            print('===> Saldo insuficiente para realizar o saque.')
        else:
            self.saldo -= valor_saque
            self.extrato.append(f'Saque: R$ {valor_saque:.2f}')
            self.saques_realizados += 1
            print(mensagem_operação)
            time.sleep(2)
            print(f'===> Contando notas.')
            time.sleep(2)
            print(f'===> Retire seu dinheiro.')
            time.sleep(2)
            print(f'===> Saque de R${valor_saque:.2f} realizado com sucesso!')
            time.sleep(2)
            print(f"+==> Limte de 3 saques diários de R%500,00 por saque. Você já efetuou {self.saques_realizados} saques na data de hoje.")
            time.sleep(2)
            print(mensagem_comprovante)
            time.sleep(2)
            print(f"\nSaldo Atual: R$ {self.saldo:.2f}")

    def extrato_bancario(self):
        print("\n------- Extrato Bancário -------")
        if not self.extrato:
            print('Não foram realizadas movimentações.')
        else:
            for movimento in self.extrato:
                print(movimento)
        print(f"\nSaldo Atual: R$ {self.saldo:.2f}")

menu_pricipal = """
Escolha uma das opções abaixo:
[1] Saque
[2] Depósito
[3] Extrato
[9] Sair

=> """

# Início #
if __name__ == "__main__":
    conta = ContaBancaria()
    
    while True:
        opcao = input(menu_pricipal)
        try:
            if opcao == '1':
                valor_saque = float(input("Digite o valor do saque: "))
                conta.sacar(valor_saque)
                time.sleep(2)
            elif opcao == '2':
                valor_deposito = float(input("Digite o valor do depósito: "))
                conta.depositar(valor_deposito)
                time.sleep(2)
            elif opcao == '3':
                conta.extrato_bancario()
            elif opcao == '9':
                print(f"Obrigado por usar nossos serviços.")
                time.sleep(2)
                break 
            else:
                print("===> Opção inválida, tente novamente.")
                time.sleep(2)
        except ValueError:
            print("===> Digite um valor válido e maior que zero.")
            time.sleep(2)