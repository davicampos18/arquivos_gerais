""" 
Vamos simular o estoque de um mercadinho onde vc implementará 
um menu com as seguintes opções:

- Cadastrar produto
- Atualizar produto
- Deletar produto
- Visualizar produtos

Utilize listas, dicionários, loops 
"""

 # Módulo para criar a tabela
from tabulate import tabulate

banco_de_dados = []
id = 0

while True:
#Menu de simulação para estoque
  print("------------------ Cadastro de Mercadorias -----------------\n")
  print("1 - Cadastrar Produto")
  print("2 - Visualizar produtos")
  print("3 - Atualizar Produto")
  print("4 - Deletar produto")
  print("5 - Sair\n")
  print("------------------------------------------------------------\n")

  #Solicitar ao usuário que digite uma das opções do menu
  escolha = int(input("Digite uma das opções anteriores: "))

  #Mach Case para verificar a opção que o usuário escolheu no menu
  match escolha:
     # 1° caso, realizar o cadastro de novos produtos
     case 1:
       #Preciso inserir na lista um dicionário:
       #Esse dicionário precisa conter:
       # Nome, Preço, Quantidade, Custo, Status = True
       print("\n======================= Cadastrar Produto ==================\n")
       nome = input("Digite o nome do produto: ")
       preco = float(input(f"Digite o preço do produto {nome}: "))
       quantidade = int(input(f"Digite a quantidade do produto {nome}: "))
       custo = float(input(f"Digite o custo do produto {nome}: "))
       # Verificar se o banco de dados está vazio, se ele estiver o ID será igual a 1, se não ele fará a soma de ID + 1
       if not banco_de_dados:
        id = 1
       else:
         id += 1

       # Cria o dicionário com os dados do produto cadastrado
       produto = {
         'ID':id,
         'Nome':nome,
         'Preço':preco,
         'Quantidade':quantidade,
         'Custo':custo,
         "Status":'Ativo'
       }
      # Insere esse dicionário na lista/banco de dados
       banco_de_dados.append(produto)
       print("Produto Cadastrado!\n")
       # 2° Caso, exibe uma tabela com os produtos cadastrados  
     case 2:
        print("\n============ Esses são os Produtos Cadastrados ===========\n")
        print(tabulate(banco_de_dados, headers="keys", tablefmt="grid"))
      # 3° Caso, atualizar as informações de um produto já cadastrado
     case 3:
        while True:
          # Primeiro mostrar ao usuário os produtos cadastrados
          print("\n============ Esses são os Produtos Cadastrados ===========\n")
          print(tabulate(banco_de_dados, headers="keys", tablefmt="grid"))

          # Solicitar ao usuário que digite o ID do produto que ele deseja modificar
          modificar_id = int(input("\nDigite o ID do produto que você deseja modoificar (Ou 0 para Sair): "))
          if modificar_id != 0:
            # Solicitar ao usuário para escolher qual opção ele deseja alterar no cadastro do produto
            alteracao = int(input("\n 1 - Nome\n 2 - Preço\n 3 - Quantidade\n 4 - Custo\n 5 - Status \nConforme o menu acima, digite o quê você quer alterar(Somente Números): "))
            match alteracao:
              case 1:
                banco_de_dados[modificar_id-1]['Nome'] = input("Digite o novo nome do produto: ")
                print("Alterado")
                continue
              case 2:
                banco_de_dados[modificar_id-1]['Preço'] = preco = float(input("Digite o novo preço do produto: "))
                print("Alterado")
                continue
              case 3:
                banco_de_dados[modificar_id-1]['Quantidade'] = input("Digite a nova quantidade do produto: ")
                print("Alterado")
                continue
              case 4:
                banco_de_dados[modificar_id-1]['Custo'] = input("Digite o novo custo do produto: ")
                print("Alterado")
                continue
              case 5:
                confirmacao = input("Deseja realmente alterar o status [S/N]")
                if confirmacao.upper() == "S":
                  if banco_de_dados[modificar_id-1]['Status'] == 'Ativo':
                    banco_de_dados[modificar_id-1]['Status'] = 'Inativo'
                    print("Status do produto desativado")
                    continue
                  else:
                    banco_de_dados[modificar_id-1]['Status'] = 'Ativo'
                    print("Status do produto ativado")
                    continue
                else:
                  print("Saindo...")
                  break
    # Caso 4, deletar um produto do banco de dados
     case 4:
        print(tabulate(banco_de_dados, headers="keys", tablefmt="grid"))
        deletar_id = int(input("\nDigite o ID do produto que você deseja deletar: "))
        banco_de_dados.pop(deletar_id-1)
        print("Produto deletado com sucesso!")
    # Caso 5, Sair do programa  
     case 5:
        confirmacao = input("Deseja realmente sair [S/N]? ")
        if confirmacao.upper() == "S":
          print("Saindo do Cadastro de Mercadorias......")
          break