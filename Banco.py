Saldo = 200
Deposito = 0
Saque = 0
Quantidade_Saque_Dia = 0
Extrato = ""
LIMITE_MAXIMO_POR_SAQUE = 500

MENU = '''======Bem vindo ao Banco DIO======
    [1] Depositar
    [2] Saque
    [3] Extrato
    [4] Sair
    Escolha uma Opção de Operação: '''
MENU_DEPOSITO = """
    [1] Realizar Deposito
    [2] Voltar pro Menu Anterior
    Escolha: """
MENU_SAQUE = '''
    [1] Realizar Saque
    [2] Voltar pro Menu Anterior
    Escolha: '''
MENU_EXTRATO = '''
    [1] Visualizar Extrato
    [2] Voltar pro Menu Anterior
    Escolha: '''
    
Operacao = int(input(MENU))

while True:
    if(Operacao == 1):
            print("======Depositar======")
            Escolha = int(input(MENU_DEPOSITO))
            if(Escolha == 1):
                Deposito = int(input("Digite o Valor do Deposito:"))
                if(Deposito > 0):
                    Saldo += Deposito
                    Extrato += ("+ R$") + str(Deposito) + (".00\n")
                    print(f"Seu novo Saldo é R$ {Saldo:.2f}")
                    Escolha = int(input(MENU_DEPOSITO))
                else:
                    print(f"Valor do Deposito deve ser acima de R$ 0,00")
            if(Escolha == 2):
                Operacao = int(input(MENU))
                
    elif(Operacao == 2):
        print("======Saque======")
        Escolha = int(input(MENU_SAQUE))
        if(Escolha == 1):
            print(f"Saldo Atual: {Saldo:.2f}")
            Saque = int(input("Digite o Valor do Saque:"))
            if(Saque<=Saldo and Saque<=LIMITE_MAXIMO_POR_SAQUE and Quantidade_Saque_Dia<=3):
                Saldo -= Saque
                Quantidade_Saque_Dia += Quantidade_Saque_Dia + 1
                print(f"Valor de R$ {Saque:.2f} Sacado")
                Extrato += ("- R$") + str(Saque) + (".00\n")
                print( f"Saldo Disponível {Saldo:.2f}")
            elif(Saque>LIMITE_MAXIMO_POR_SAQUE):
                print("Valor de Saque excede o Valor permitido por Transação")
            elif(Saque>Saldo):
                print("Saldo Insuficiente!")
            elif(Quantidade_Saque_Dia>3):
                print("Limite de Saque Diarios Permitido Alcançado")
        
        if(Escolha == 2):
            Operacao = int(input(MENU))
    
    
    elif(Operacao == 3):
        print("======Extrato======")
        Escolha = int(input(MENU_EXTRATO))
        if(Escolha == 1):
            print("Imprimindo Extrato:")
            print(Extrato)
            print(f"Saldo Atual: {Saldo:.2f}")
        if(Escolha == 2):
            Operacao = int(input(MENU))
            
    elif(Operacao == 4):
            print("Obrigado pela Preferência")
            break
    else:
        (print("Opção Incorreta"))
        Operacao = int(input(MENU))