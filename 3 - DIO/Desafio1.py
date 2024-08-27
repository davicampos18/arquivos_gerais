saldo = 0

contador_de_saque = 3

extrato = []

# Primeiro: Criar um loop para exibir as opções ao usuário
while True:
    print("""        Banco Campos - Caixa Eletrônico
          
1 - Extrato
2 - Depósito
3 - Saque
4 - Finalizar Operação

""")
    operacao = int(input("Digite uma das opções acima (Apenas número): "))

    # if para direcionar a 1° opção, criar um for para iterar sobre a minha tupla, logo após criar um if para verificar se o valor é positivo, se sim é um valor depósitado
    # criar um elif para verificar se o valor é negativo, se sim é um valor de saque
    if operacao == 1:
        print("\nEXTRATO\n")
        for valor in extrato:
            if valor > 0:
                print(f"Valor Depósitado R$ {valor:.2f}")
            elif valor < 0:
                print(f"Valor Sacado R$ {valor:.2f}")
        print(f"\nSaldo Atual R$ {saldo:.2f}\n")
        continue
    elif operacao == 2:
        print("\nOPERAÇÃO DE DEPÓSITO\n")
        deposito = float(input("Qual valor você deseja depositar R$ "))
        saldo += deposito
        extrato.append(deposito)
        print(f"\nO valor de R$ {deposito:.2f} foi depósitado a sua conta\nSaldo Atual R$ {saldo:.2f}\n")
        continue

    elif operacao == 3:
        print("\nOPERAÇÃO DE SAQUE\n")
        while True:
            if contador_de_saque != 0:
                saque = float(input("Qual valor deseja sacar R$ "))
                if saque >= 1 and saque <= 500:
                    if saldo >= saque:
                        saldo -= saque
                        valor_saque = saque - (saque * 2)
                        extrato.append(valor_saque)
                        print(f"Valor de R$ {saque:.2f} retirado da conta\nSaldo atual R$ {saldo:.2f}\n")
                        contador_de_saque -= 1
                        break
                    elif saldo < saque and saldo != 0:
                        print(f"\nSALDO INSUFICIENTE!\nSeu saldo é de R$ {saldo:.2f}\nDigite um valor igual ou menor ao seu saldo!")
                        continue
                    elif saldo == 0:
                        print(f"Seu saldo é de R$ {saldo:.2f}. Depósite um valor ou finalize a operação!\n")
                        break
                    else:
                        print("Valor Incorreto! Tente Novamente!")
                else:
                    print("ATEÇÃO!!!!\nNão permitimos saques acima de R$ 500.00 por gentileza digite outro valor")
                    continue
            else:
                print("Você atingiu o limite de saques (3 Saques), tente novamente amanhã!\n")
                break

    # elife para direcionar a 4° opção, primeiro exibir uma mensagem e depois para o loop com o break
    elif operacao == 4:
        print("\nFinalizando Operação.......")
        break
    
    # else para caso o usuário digite um número que não esteja no menu
    else:
        print("\n--------- Valor Inválido!!!! Digite um valor válido. ---------\n")
        continue
