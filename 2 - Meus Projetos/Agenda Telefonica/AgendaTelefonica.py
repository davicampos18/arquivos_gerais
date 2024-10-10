# Criar uma agenda telefonica para armazenar nome, telefone, endereço de e-mail:
# Funcionalidades

# 1 - Deve registrar os contatos;
# 2 - Permitir que o usuário atualize o contato
# 3 - Permirir a exclusão do contato
# 4 - Permitir a consulta de um contato específico
# 5 - Permitir a visualização de todos os contatos


# Primeiro: Importar o tabulate para criar a grade na solicitação de todo os contatos
from tabulate import tabulate

# Segundo: Criar uma função para localizar informações no banco de dados
def localizar_contato(dicionarios, localizacao):
  for indice, contato in enumerate(dicionarios):
      if localizacao.lower() in [value.lower() for value in contato.values()]:
          return indice
  return -1

# Terceiro: Criar uma lista para ser o nosso banco de dados
contatos = []

# Quarto: Criar um loop e exibir o menu da agenda
while True:

  # Quinto: Exibir as opções da agenda
  print("Agenda Telefônica\n")
  print("OPÇÕES DA AGENDA:\n1 - Registrar Novo Contato;\n2 - Atualizar Contato;\n3 - Excluir Contato;\n4 - Visualizar Contato;\n5 - Visualizar Contatos;\n6 - Encerrar Aplicação.")

  # Sexto: Solicitar ao usuário que digite uma das opções acima
  opcao = int(input("\nDigite uma das opções acima (Somente Números): "))

  # Sétimo: Criar um match-case para direcionar o usuário para a opção escolhida
  match opcao:
    # Oitavo: Encerrar a agenda
    case 6:
      print("\nSaindo da agenda.......")
      break
    # Nono: Cadastrar um novo contato  
    case 1:
      print("\nCadastro de Contato\n")
      # Décimo: Solicitar ao usuário que forneça as informações do contato a ser cadastrado
      nome = input("Digite o nome do contato: ")
      numero = input("Digite o número do contato (Sem traços, parênteses, somente números): ")
      email = input("Digite o e-mail do contato: ")

      # Décimo-Primeiro: Criar um dicionário, depois inserir na lista de dicionários
      contato = {
        "Nome":nome,
        "Número":numero,
        "E-mail":email
      }
      contatos.append(contato)
      print("Contato Registrado!\n")

    # Décimo-Segundo: Exibir opções para atualizar as informações de um contato
    case 2:
      # Décimo-Terceiro: Solicitar ao usuário que digite um parâmetro para encontrar o contato a ser atualizado
      localizacao = input("\nDigite o nome, telefone ou e-mail do contato que está querendo alterar: ")
      # Décimo-Quarto: Localizar a posição do contato na lista de dicionários
      posicao = localizar_contato(contatos, localizacao)

      # Décimo-Quinto: Verificar qual o valor retornou da função
      if posicao != -1:
        # Décimo-Sexto: Retornar a posição do contato
        contato_encontrado = contatos[posicao]

        # Décimo-Sétimo: Exibir as informações de modificação
        alteracao_contato = int(input("\nOPÇÕES D MODIFICAÇÃO:\n1 - Nome\n2 - Número\n3 - E-mail\nDigite uma das opções acima(Somente Números): "))

        # Décimo-Oitavo: match-case para direcionar o usuário a opção escolhida
        match alteracao_contato:
          # Décimo-Nono: Atualizar o nome do contato
          case 1:
            contato_encontrado["Nome"] = input("Digite o novo nome do contato: ")
            print("Nome do Contato Alterado!\n")
          # Vigésimo: Atualizar o número do contato
          case 2:
            contato_encontrado["Número"] = input("Digite o novo número do contato (Sem traços, parênteses, somente números): ")
            print("Número do Contato Alterado!\n")
          # Vigésimo-Primeiro: Atualizar o e-mail do contato
          case 3:
            contato_encontrado["E-mail"] = input("Digite o novo E-mail do contato: ")
            print("E-mail do Contato Alterado!\n")

    # Vigésimo-Segundo: Deletar um contato
    case 3:
      localizacao = input("\nDigite o nome, telefone ou e-mail do contato que está procurando: ")
      posicao = localizar_contato(contatos, localizacao)
      contatos.pop(posicao)
      print("Contato Excluído com Sucesso!")

    case 4:
        localizacao = input("\nDigite o nome, telefone ou e-mail do contato que está procurando: ")
        posicao = localizar_contato(contatos, localizacao)

        if posicao != -1:
          contato_encontrado = contatos[posicao]
          print(f"\nO contato está cadastrado com as seguintes informações:\nNome: {contato_encontrado['Nome']}\nNúmero: {contato_encontrado['Número']}\nE-mail: {contato_encontrado['E-mail']}\n")
        else:
          print("\nContato não encontrado!")
    case 5:
      print("\n"+tabulate(contatos, headers="keys", tablefmt="grid")+"\n")