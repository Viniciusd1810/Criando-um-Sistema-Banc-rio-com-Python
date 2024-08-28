Deposito = 0
Saque = 0
Saldo = 0
Extrato = ""
Quantidade_Saque_Dia = 0

MENU = '''======Bem vindo ao Banco DIO======
    [1] Depositar
    [2] Saque
    [3] Extrato
    [4] Cadastro de Clientes
    [5] Sair
    Escolha uma Opção de Operação: '''

# DEFINIÇÃO DA FUNÇÃO DE DEPOSITO
# ELA SOMA VALORES ACIMA DE 0 AO SALDO
# ELA TEM COMO RETORNO O SALDO E O EXTRATO
def funcao_deposito(Deposito, Saldo, Extrato):
    Deposito = int(input("Digite o Valor Para Depositar:"))
    if(Deposito > 0):
        Saldo += Deposito
        Extrato += ("+ R$") + str(Deposito) + (".00\n")
        print(f"Seu novo Saldo é R$ {Saldo:.2f}")
        return Saldo, Extrato
    else:
        print(f"Valor do Deposito deve ser acima de R$ 0,00")

# DEFINIÇÃO DA FUNÇÃO DE SAQUE
# ELA SUBTRAI DO SALDO VALORES MAIORES QUE 0
# O LIMITE DE VALOR MAXIMO POR SAQUE É 500
# TEM O LIMITE DE 3 SAQUES POR USO
# RETORNA O SAQUE, SALDO, EXTRATO E QUANTIDADE DE SAQUE POR DIA
def funcao_saque(Saque, Saldo, Extrato, Quantidade_Saque_Dia):
    LIMITE_MAXIMO_POR_SAQUE = 500

    print(f"Saldo Atual: {Saldo:.2f}")
    Saque = int(input("Digite o Valor do Saque:"))
    if(Saque<=Saldo and Saque<=LIMITE_MAXIMO_POR_SAQUE and Quantidade_Saque_Dia<=3):
        Saldo -= Saque
        Quantidade_Saque_Dia += Quantidade_Saque_Dia + 1
        print(f"Valor de R$ {Saque:.2f} Sacado")
        Extrato += ("- R$") + str(Saque) + (".00\n")
        print( f"Saldo Disponível {Saldo:.2f}")
        return Saldo, Extrato, Quantidade_Saque_Dia
    
    elif(Saque>LIMITE_MAXIMO_POR_SAQUE):
        print("Valor de Saque excede o Valor permitido por Transação")
        return Saldo, Extrato, Quantidade_Saque_Dia

    elif(Saque>Saldo):
        print("Saldo Insuficiente!")
        return Saldo, Extrato, Quantidade_Saque_Dia

    elif(Quantidade_Saque_Dia>3):
        print("Limite de Saque Diarios Permitido Alcançado")
        return Saldo, Extrato, Quantidade_Saque_Dia

# DEFINIÇÃO DA FUNÇÃO DE EXTRATO
# ELA IMPRIME O EXTRATO QUE FOI RECIBIDO DE OUTRAS FUNÇÕES
# ELA RETORNA O SALDO E EXTRATO 
def funcao_extrato(Saldo, Extrato):
    print("Imprimindo Extrato:")
    print(Extrato)
    print(f"Saldo Atual: {Saldo:.2f}")
    return Saldo, Extrato

def funcao_cadastro_de_clientes():

        
Operacao = int(input(MENU))

while True:
    if(Operacao == 1):
        print("======Depositar======")
        Saldo, Extrato = funcao_deposito(Deposito, Saldo, Extrato)
        Operacao = int(input(MENU))

    elif(Operacao == 2):
        print("======Saque======")
        Saldo, Extrato, Quantidade_Saque_Dia = funcao_saque(Saque, Saldo, Extrato, Quantidade_Saque_Dia)
        Operacao = int(input(MENU))

    elif(Operacao == 3):
        print("======Extrato======")
        Saldo, Extrato = funcao_extrato(Saldo, Extrato)
        Operacao = int(input(MENU))
    
    elif(Operacao == 4):
        print("=====Cadastro de Clientes====")

    elif(Operacao == 5):
        print("Obrigado pela Preferência")
        break
    
    else:
        (print("Opção Incorreta"))
        Operacao = int(input(MENU))
