#Seção de Importações

from datetime import datetime, timedelta

# Flags para armazenar os valor do saldo e limite de transações diárias
valor_em_conta = [0]
contador_transacao= [10]
# lista para adicionar os valores de deposito e saque para exibir no extrato
informacoes_extrato = []

# Funções

def extrato():
# Criar um for para iterar sobre a minha lista, logo após criar um if para verificar se o valor é positivo, se sim é um valor depósitado
# Criar um elif para verificar se o valor é negativo, se sim é um valor de saque
    data_atual = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    if len(informacoes_extrato) != 0:
        for valores in range(0, len(informacoes_extrato)):
            valor_em_analise = informacoes_extrato[valores]["Valor"]
            data_em_analise = informacoes_extrato[valores]["Data"]
            if valor_em_analise > 0:
                    print(f"Valor Depósitado R$ {valor_em_analise:.2f} ({data_em_analise})")
            elif valor_em_analise < 0:
                    print(f"Valor Sacado R$ {valor_em_analise:.2f} ({data_em_analise})")
        return f"\nSaldo Atual R$ {valor_em_conta[0]:.2f} - {data_atual}\n"
    else:
        return f"Você não tem nenhum valor depósitado à sua conta.\n"
   
def deposito(valor_deposito:float, saldo:list):
# Somar o valor de depósito com o valor do saldo
    saldo[0] += valor_deposito
    depositar =  {"Valor":valor_deposito,
                  "Data":datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
                  }
    informacoes_extrato.append(depositar)
    return f"\nO valor de R$ {valor_deposito:.2f} foi depósitado à sua conta.\nSaldo Atual R$ {saldo[0]:.2f} - {datetime.now().strftime("%d/%m/%Y, %H:%M:%S")}\n"

def saque(valor_a_ser_sacado:float, saldo:list, contador:list):
# Subtrair o valor de saldo que pelo saque
    saldo[0] -= valor_a_ser_sacado
    valor_saque = valor_a_ser_sacado - (valor_a_ser_sacado * 2)
    sacar = {"Valor":valor_saque,
             "Data":datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
             }
    informacoes_extrato.append(sacar)
    contador[0] -= 1
    print(f"A quantia noo valor de R$ {valor_a_ser_sacado:.2f} foi retirado da sua conta na data de {datetime.now().strftime("%d/%m/%Y")}.\nSaldo atual R$ {saldo[0]:.2f} - {datetime.now().strftime("%d/%m/%Y, %H:%M:%S")}\n")
    

# Criar um loop para exibir o menu
while True:
    print("""        Banco Campos - Caixa Eletrônico
          
1 - Extrato
2 - Depósito
3 - Saque
4 - Finalizar Operação

""")
    operacao = int(input("Digite uma das opções acima (Apenas número): "))

    match operacao:
        case 1:
            # Chamar a função extrato
            print("\nEXTRATO\n")
            print(extrato())
            continue
        case 2:
            # Solicitar ao usuário que digite o valor à ser depósitado e chamar a função de depósito
            print("\nOPERAÇÃO DE DEPÓSITO\n")
            while True:
                valor_de_deposito = float(input("Quanto você deseja depositar R$ "))
                if valor_de_deposito <= 0:
                    print("\nATENÇÃO\nNão aceitamos valores negativos ou iguais a 0, deposite um valor válido!")
                elif valor_de_deposito > 0:
                    print(deposito(valor_de_deposito, valor_em_conta))
                    break
                else:
                    print("Valor Inválido!")
        case 3:
            print("\nOPERAÇÃO DE SAQUE\n")
            while True:
                if contador_transacao != 0:
                    valor_de_saque = float(input("Qual valor você deseja sacar R$ "))
                    if (valor_de_saque >= 1 and valor_de_saque <= 500) and valor_em_conta[0] >= valor_de_saque:
                        print(saque(valor_de_saque, valor_em_conta, contador_transacao))
                        break
                    elif valor_em_conta[0] < valor_de_saque and valor_em_conta[0] != 0:
                        print(f"\nSALDO INSUFICIENTE!\nSeu saldo é de R$ {valor_em_conta[0]:.2f}\nDigite um valor igual ou menor ao seu saldo!")
                        continue
                    elif valor_em_conta[0] == 0:
                        print(f"Seu saldo é de R$ {valor_em_conta[0]:.2f}. Depósite um valor ou finalize a operação!\n")
                        break
                    elif valor_de_saque > 500:
                        print("\nATEÇÃO!!!!\nNão permitimos saques acima de R$ 500.00 por gentileza digite outro valor\n")
                        continue
                    else:
                        print("Valor Incorreto! Tente Novamente!")
                else:
                    hora_para_novas_transacoes = datetime.now() + timedelta(days=1)
                    print(f"Você atingiu o limite de saques (10 Saques por dia), tente novamente amanhã {hora_para_novas_transacoes.strftime("%d/%m/%Y")}!\n")
                    break
        case 4:
            print("\nFinalizando Operação....\n")
            break
        case _:
             print("\n--------- Valor Inválido!!!! Digite um valor válido. ---------\n")