import time
from datetime import datetime
mensagem_comprovante = "===> Aguarde a impressão do comprovante de depósito\n"
mensagem_operação = "===> Efetuando operação.  Aguarde."
encerra_operacao = False
LIMITE_SAQUES_DIARIOS = 3
LIMITE_VALOR_SAQUE = 500
clientes_pf = {}
clientes_pj = {}
contas_pf = {}
contas_pj = {}

class Cliente:
    def __init__(self):
        self.cpf_cnpj = 0
        self.info = ""
        self.nome = ""
        self.data_nasc = ""
        self.endereco = ""
        self.tipo_pessoa = ""
        
    def cadastrar_cliente(self):
        # Recebe tipo pessoa
        msg_informacao_invalida = "==> Tipo pessoa inválido. Tente novamente."
        self.tipo_pessoa = valida_tipo_pessoa("Informe J (Pessoa Jurídica) ou F (Pessoa Física): ", msg_informacao_invalida)
        
        if self.tipo_pessoa == "F":
            # Recebe cpf
            msg_informacao_invalida = "==> CPF inválido. Tente novamente."
            self.cpf_cnpj = valida_entrada("Informe CPF (somente números): ", 11, 11, "S", "N", msg_informacao_invalida)

            if self.cpf_cnpj in clientes_pf:
                print("==> CPF já cadastrado!")
                time.sleep(1)
                print("==> Retornando ao menu anterior.")
                time.sleep(1)
                return False
                
            self.data_nasc = valida_data("Informe data nasc. (DD/MM/AAAA): ")
            print(f"Data formatada: {self.data_nasc}")
            msg_informacao_invalida = "==> Nome deve ter mínimo de 2 e  máximo de 60 caracteres."
            self.nome = valida_entrada("Informe seu nome: ", 2, 60,"N","N", msg_informacao_invalida)      
            
            msg_informacao_invalida = "==> Logradouro deve ter mínimo de 20 e máximo de 80 caracteres."
            self.endereco = valida_entrada("Digite o endereço (logradouro, número - bairro - cidade/sigla estado): ", 20, 80,"N","N", msg_informacao_invalida) 
            
            # Adiciona o usuário à lista
            clientes_pf[self.cpf_cnpj] = {
                'nome': self.nome,
                'data_nascimento': self.data_nasc,
                'endereco': self.endereco,
                'contas': []
            }
            print("==> Cliente cadastrado com sucesso.")
            time.sleep(1)
            print("==> Retornando ao menu anterior.")
            time.sleep(1)
            return True
        else:
            # Recebe cnpj
            msg_informacao_invalida = "==> CNPJ inválido. Tente novamente."
            self.cpf_cnpj = valida_entrada("Informe CNPJ (somente números): ", 14, 14, "S", "N", msg_informacao_invalida)

            if self.cpf_cnpj in clientes_pj:
                print("==> CNPJ já cadastrado!")
                time.sleep(1)
                print("==> Retornando ao menu anterior.")
                time.sleep(1)
                return False
                
            msg_informacao_invalida = "==> Nome deve ter mínimo de 2 e  máximo de 60 caracteres."
            self.nome = valida_entrada("Informe nome da empresa: ", 2, 60,"N","N", msg_informacao_invalida)      
            
            msg_informacao_invalida = "==> Logradouro deve ter mínimo de 20 e máximo de 80 caracteres."
            self.endereco = valida_entrada("Digite o endereço (logradouro, número - bairro - cidade/sigla estado): ", 20, 80,"N","N", msg_informacao_invalida) 
            
            # Adiciona o usuário à lista
            clientes_pj[self.cpf_cnpj] = {
                'nome': self.nome,
                'endereco': self.endereco,
                'contas': []
            }
            print("==> Cliente cadastrado com sucesso.")
            time.sleep(1)
            print("==> Retornando ao menu anterior.")
            time.sleep(1)
            return True

class Conta:
    def __init__(self):
        self.cpf_cnpj = 0 
        self.agencia = 0
        self.conta = 0
        self.digito = 0
        self.tipo_conta = ""
        
    def cadastrar_conta(self):
        # Recebe cpf ou cnpj
        msg_informacao_invalida = "==> CPF ou CNPJ inválido. Tente novamente."
        self.cpf_cnpj = input("Informe CPF ou CNPJ (somente números): ")
        
        if self.cpf_cnpj not in clientes_pf and self.cpf_cnpj not in clientes_pj:
            print("==> Cliente não cadastrado!")
            time.sleep(1)
            print("==> Retornando ao menu anterior.")
            time.sleep(1)
            return False
        elif self.cpf_cnpj in clientes_pf:
            self.tipo_pessoa = "F"
        elif self.cpf_cnpj in clientes_pj:
            self.tipo_pessoa = "J"
            
        msg_informacao_invalida = "==> Agência deve ter 4 algarismos."
        self.agencia = valida_entrada("Informe o número da agência com 4 algarismos: ", 4, 4,"S","N", msg_informacao_invalida) 

        msg_informacao_invalida = "==> Conta deve ter 5 algarismos."
        self.conta = valida_entrada("Informe o número da conta com 5 algarismos: ", 5, 5,"S","N", msg_informacao_invalida) 

        msg_informacao_invalida = "==> Dígito deve ter 1 número."
        self.digito = valida_entrada("Informe dígito da conta com 1 algarismo: ", 1, 1,"S","N", msg_informacao_invalida) 
        
        msg_informacao_invalida = "==> Tipo de conta inválida."
        self.tipo_conta = valida_tipo_conta("Informe tipo de conta CC (Conta Corrente) ou P (Poupança)): ", msg_informacao_invalida) 
        
        # valida se conta já está associada a algum cliente
        if self.tipo_pessoa == "F":
            if (self.agencia, self.conta, self.digito) in contas_pf:
                print(f"==> Já existe cadastro para a conta: {self.agencia}-{self.conta}-{self.digito}.")
                time.sleep(1)
                print("==> Retornando ao menu anterior.")
                time.sleep(1)
                return False
            
            contas_pf[(self.agencia, self.conta, self.digito)] = {
                'tipo': self.tipo_conta,
                'saldo': 0.0,
                'saques': [],
                'depositos': [],
                'saques_diarios': 0
            }
            clientes_pf[self.cpf_cnpj]['contas'].append((self.agencia, self.conta, self.digito))

        elif self.tipo_pessoa == "J":
            if (self.agencia, self.conta, self.digito) in contas_pj:
                print(f"==> Já existe cadastro para a conta: {self.agencia}-{self.conta}-{self.digito}.")
                time.sleep(1)
                print("==> Retornando ao menu anterior.")
                time.sleep(1)
                return False
            
            contas_pj[(self.agencia, self.conta, self.digito)] = {
                'tipo': self.tipo_conta,
                'saldo': 0.0,
                'saques': [],
                'depositos': [],
                'saques_diarios': 0
            }
            clientes_pj[self.cpf_cnpj]['contas'].append((self.agencia, self.conta, self.digito))

        print(f"==> Conta cadastrada com sucesso: Agência {self.agencia} e Conta {self.conta} - {self.digito}.")
        return True

    def listar_contas(self):
        # Lista as informações de todos os clientes e suas contas.
        if not clientes_pf:
            print("==> Não há clientes Pessoa Física cadastrados.")
        else:
            for cpf, info in clientes_pf.items():
                print(f"\n=== Informações do Cliente ===")
                print(f"Nome Titular: {info['nome']}")
                if info['contas']:
                    for agencia, conta, digito in info['contas']:
                        print(f"==> Agência: {agencia}  Conta: {conta} - {digito}")
                else:
                    print("==> Nenhuma conta cadastrada.")

        if not clientes_pj:
            print("==> Não há clientes Pessoa Jurídica cadastrados.")
        else:
            for cnpj, info in clientes_pj.items():
                print(f"\n=== Informações do Cliente ===")
                print(f"Nome Titular: {info['nome']}")
                if info['contas']:
                    for agencia, conta, digito in info['contas']:
                        print(f"==> Agência: {agencia}  Conta: {conta} - {digito}")
                else:
                    print("==> Nenhuma conta cadastrada.")

class MovimentacaoBancaria:
    def __init__(self):
        self.saldo = 0.0
        self.extrato = []
        self.qtd_saques_dia = 0
        self.agencia = 0
        self.conta = 0
        self.digito = 0

    def solicitar_agencia_conta(self):
        msg_informacao_invalida = "==> Agência deve ter 4 algarismos."
        self.agencia = valida_entrada("Informe o número da agência com 4 algarismos: ", 4, 4, "S","N", msg_informacao_invalida) 
        
        # def valida_entrada(prompt, tamanho_minimo, tamanho_maximo, numerico, opcional, msg_informacao_invalida):

        msg_informacao_invalida = "==> Conta deve ter 5 algarismos."
        self.conta = valida_entrada("Informe o número da conta com 5 açgarismos: ", 5, 5,"S","N", msg_informacao_invalida) 

        msg_informacao_invalida = "==> Dígito deve ter 1 número."
        self.digito = valida_entrada("Informe dígito da conta com 1 algarismo: ", 1, 1,"S","N", msg_informacao_invalida) 

        print(f"\nInformações fornecidas:")
        print(f"Agência : {acesso_conta.agencia}")
        print(f"Conta   : {acesso_conta.conta}-{acesso_conta.digito}")

        # verifica se conta está cadastrada
        if (self.agencia, self.conta, self.digito) in contas_pf:
            self.tipo_conta = "F"
            return self.agencia, self.conta, self.digito, self.tipo_conta
        elif (self.agencia, self.conta, self.digito) in contas_pj:
            self.tipo_conta = "J"
            return self.agencia, self.conta, self.digito, self.tipo_conta
        else:    
            print("==> Conta não cadastrada!")
            time.sleep(1)
            print("==> Retornando ao menu anterior.")
            time.sleep(1)
            return False


    def recuperar_conta(self):
        if (self.agencia, self.conta, self.digito) in contas_pf:
            return contas_pf[(self.agencia, self.conta, self.digito)], "F"
        elif (self.agencia, self.conta, self.digito) in contas_pj:
            return contas_pj[(self.agencia, self.conta, self.digito)], "J"
        else:
            print("==> Conta não cadastrada!")
            return None, None
        
    def depositar(self, valor_deposito):
        if valor_deposito > 0:
            conta_info, tipo_conta = self.recuperar_conta()
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            if conta_info is None:
                return

            conta_info['saldo'] += valor_deposito
            conta_info['depositos'].append((valor_deposito, data_hora))
            self.saldo = conta_info['saldo']
            
            print(mensagem_operação)
            time.sleep(2)
            print(f'===> Depósito no valor de R$ {valor_deposito:.2f} efetuado com sucesso.')
            time.sleep(2)
            print(f"Saldo atual:  {formatar_valor(self.saldo)}.")
            print(mensagem_comprovante)
            self.qtd_saques_dia += 1
        else:
            print('===>Valor de depósito deve ser maior que zero.')

    def sacar(self, valor_saque):
        conta_info, tipo_conta = self.recuperar_conta()
        # data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        if conta_info is None:
            return
        
        self.saldo = conta_info['saldo']

        if self.qtd_saques_dia > LIMITE_SAQUES_DIARIOS:
            print('===> Limite de transações diárias atingido para a data de hoje.')
            return
        elif valor_saque > LIMITE_VALOR_SAQUE:
            print(f'===> O valor do saque não pode ser maior que R$ {LIMITE_VALOR_SAQUE:.2f}.')
            return
        elif valor_saque > self.saldo:
            print('===> Saldo insuficiente para realizar o saque.')
            return
        
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        conta_info['saldo'] -= valor_saque
        conta_info['saques'].append((valor_saque, data_hora))
        conta_info['saques_diarios'] += 1
        self.qtd_saques_dia += 1
        self.saldo = conta_info['saldo']
        print(mensagem_operação)
        time.sleep(2)
        print(f'===> Contando notas.')
        time.sleep(2)
        print(f'===> Retire seu dinheiro.')
        time.sleep(2)
        print(f"Saque de {formatar_valor(valor_saque)} realizado com sucesso.")
        time.sleep(2)
        print(mensagem_comprovante)
        time.sleep(2)
        print(f"Saldo atual:  {formatar_valor(self.saldo)}.")

    def extrato_bancario(self, tipo_conta):
        conta_info, tipo_conta = self.recuperar_conta()
        # data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        if conta_info is None:
            return
               
        print(f"\nExtrato da Conta - Agência: {self.agencia} - Conta: {self.conta}-{self.digito}")
        print(f"\nEm {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}")
               
        if not conta_info['depositos'] and not conta_info['saques']:
            print("==> Não foram realizadas movimentações.")
        else:
            transacoes = []
            if conta_info['depositos']:
                for deposito in conta_info['depositos']:
                    transacoes.append(('Depósito', deposito[0], deposito[1]))
            if conta_info['saques']:
                for saque in conta_info['saques']:
                    transacoes.append(('Saque', saque[0], saque[1]))
                    
            # Ordena as transações por data/hora
            transacoes.sort(key=lambda x: x[2])  # x[2] é a data/hora
            for tipo, valor, data in transacoes:
                print(f"- {tipo}: {formatar_valor(valor)} em {data}")
                
        print(f"Saldo atual: {formatar_valor(conta_info['saldo'])}")

def formatar_valor(valor):
    return f"R$ {valor:.2f}"

def valida_tipo_pessoa(prompt, msg_informacao_invalida):
    while True:
        user_input = input(prompt)
        user_input = user_input.strip().upper()  # Transforma tipo pessoa em maiúsculo
        if user_input in ("F","J"):
            return user_input.upper()
        else:
            print(msg_informacao_invalida)
        
def valida_tipo_conta(prompt, msg_informacao_invalida):
    while True:
        user_input = input(prompt)
        user_input = user_input.strip().upper()  # Transforma tipo pessoa em maiúsculo
        if user_input in ("CC","P"):
            return user_input.upper()
        else:
            print(msg_informacao_invalida)

            
def valida_entrada(prompt, tamanho_minimo, tamanho_maximo, numerico, opcional, msg_informacao_invalida):
    while True:
        user_input = input(prompt)
        user_input = user_input.strip()
        if opcional == "S":
            if len(user_input) == 0:
                return user_input
        else:
            if numerico == "S":
                if len(user_input) >= tamanho_minimo and len(user_input) <= tamanho_maximo and user_input.isnumeric():
                    return user_input
                else:
                    print(msg_informacao_invalida)
            else:
                if len(user_input) >= tamanho_minimo and len(user_input) <= tamanho_maximo:
                    return user_input
                else:
                    print(msg_informacao_invalida)
                

def valida_data(prompt):
    while True:
        user_input = input(prompt)
        try:
            valid_date = datetime.strptime(user_input, '%d/%m/%Y')
            valid_date = valid_date.strftime('%d/%m/%Y')
            return valid_date
        except ValueError:
            print("Data inválida. Data informada deve ser DD/MM/AAAA. Exemplo: 01/01/2000")

menu_principal = """
SISTEMA BANCÁRIO
Escolha uma das opções abaixo:
[1] Administrativo
[2] Conta Cliente
[9] Encerrar

=> """
menu_conta_cliente = """
CONTA CLIENTE
Escolha uma das opções abaixo:
[1] Saque
[2] Depósito
[3] Extrato
[4] Retorna menu anterior
[9] Encerrar

=> """

menu_admin = """
ADMINISTRATIVO
Escolha uma das opções abaixo:
[1] Nova conta
[2] Novo cliente
[3] Listar Contas
[4] Retorna menu anterior
[9] Encerrar

=> """


# Início #
if __name__ == "__main__":
    acesso_conta = MovimentacaoBancaria()
    cliente = Cliente()
    conta = Conta()
    # print(encerra_operacao)
    
    while not encerra_operacao:
        try:
            opcao = input(menu_principal)
            try:
                if opcao == '1':
                    while True:
                        opcao_adm = input(menu_admin)
                        try:
                            if opcao_adm == '1':
                                conta.cadastrar_conta()
                            elif opcao_adm == '2':
                                cliente.cadastrar_cliente()
                            elif opcao_adm == '3':
                                conta.listar_contas()
                            elif opcao_adm == '4':
                                time.sleep(1)
                                break 
                            elif opcao_adm == '9':
                                print(f"Obrigado por usar nossos serviços.")
                                time.sleep(2)
                                encerra_operacao = True
                                break 
                            else:
                                print("===> Opção inválida, tente novamente.")
                                time.sleep(2)
                        except ValueError:
                            print("===> ERRO menu_admin")
                            time.sleep(2)
                            encerra_operacao = True
                elif opcao == '2':
                     try:
                         while not encerra_operacao: 
                            if acesso_conta.solicitar_agencia_conta():
                                while True:
                                    opcao_conta = input(menu_conta_cliente)
                                    try:
                                        if opcao_conta == '1':
                                            valor_saque = float(input("Digite o valor do saque: "))
                                            acesso_conta.sacar(valor_saque)
                                            time.sleep(2)
                                        elif opcao_conta == '2':
                                            valor_deposito = float(input("Digite o valor do depósito: "))
                                            acesso_conta.depositar(valor_deposito)
                                            time.sleep(2)
                                        elif opcao_conta == '3':
                                            acesso_conta.extrato_bancario(conta.tipo_conta)
                                        elif opcao_conta == '4':
                                            time.sleep(1)
                                            break 
                                        elif opcao_conta == '9':
                                            print(f"Obrigado por usar nossos serviços.")
                                            time.sleep(2)
                                            encerra_operacao = True
                                            break 
                                        else:
                                            print("===> Opção inválida, tente novamente.")
                                            time.sleep(2)
                                    except ValueError:
                                        print("===> Digite um valor válido e maior que zero.")
                                        time.sleep(2)
                            else:
                                break                                        
                     except ValueError:
                        print("===> Informações inválidas para agência e conta.")
                        time.sleep(2)
                     except ValueError:
                         print("===> ERRO menu_principal")
                         time.sleep(2)
                         encerra_operacao = True
                
                elif opcao == '9':
                    print(f"Obrigado por usar nossos serviços.")
                    time.sleep(2)
                    encerra_operacao = True
                    break 
                else:
                    print("===> Opção inválida, tente novamente.")
                    time.sleep(2)
                    

            except ValueError:
                print("===> ERRO menu_principal")
                time.sleep(2)
                encerra_operacao = True

        except ValueError:
            print("===> ERRO operação.")
            time.sleep(2)
            encerra_operacao = True
