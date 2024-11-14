from funcoes import *

# Criar um loop para exibir o menu
while True:
    print("""        Banco Campos - Caixa Eletrônico
          
1 - Depósito
2 - Saque
3 - Extrato
4 - Cadastrar Usuário
5 - Finalizar Operação

""")
    
    operacao = int(input("Digite uma das opções acima (Apenas números): "))

    if operacao == 1 or operacao == 2 or operacao == 3:
        conta = input("Digite o número da conta: ")
        indice = pesquisar_indice(indices_das_contas, conta)
        if indice == -1:
            print(f"\nA conta com o número {conta} não existe, verifique o número e tente novamente.\n")
            continue
        else:
            if operacao == 1 or operacao == 2:
                valor = float(input("Digite o valor para prosseguir com a operação: "))
            else:
                valor = 0
            dados_da_operacao = Operacoes(usuarios, conta, indice, valor)
            print(indice)
            print(type(indice))
            match operacao:
                case 1:
                    print(dados_da_operacao.deposito())
                case 2:
                    print(dados_da_operacao.saque())
                case 3:
                    print(dados_da_operacao.tirar_extrato())
    elif operacao >= 4 or operacao <= 5:
        match operacao:
            case 4:
                cpf = input("Digite o CPF para cadastro: ")
                nome = input("Digite o Nome Completo para cadastro: ")
                data_nascimento = input("Digite a Data de Nascimento para cadastro: ")
                endereco = input("Digite o Endereço para cadastro: ")
                nome_mae = input("Digite o Nome da Mãe do usuário para cadastro: ")
                tipo_conta = input("Qual o tipo da conta: ")
                saldo = float(input("Qual o Saldo Inicial: "))

                print(cadastrar_usuario(usuarios, cpf, nome, data_nascimento, endereco, nome_mae, tipo_conta, saldo))
                print(indices_das_contas)
                print(quantidade_de_contas)
            case 5:
                print("\nFinalizando Operação....\n")
                break
    else:
        print("\n--------- Valor Inválido!!!! Digite um valor válido. ---------\n")
        continue


