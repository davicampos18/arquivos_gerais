# 1° Seção - Inportações

# Importar o tabulate para gerar uma grade na depuração de votos que irá conter o nome do candidato e a quantidade de votos
from tabulate import tabulate

# 2° Seção - Bancos de Dados
# Informações para cadastro de pessoas CPF, NOME, TÍTULO DE ELEITOR, DATA DE NASCIMENTO

# Lista de dicionários que contém as informações dos eleitores
eleitores_da_secao = [{'Nome': 'Melissa Novaes', 'Data_Nasc': '01/08/2006', 'CPF': '65564388711', 'Titulo_Eleitor': '914162022138'},
{'Nome': 'Gustavo Henrique Macedo', 'Data_Nasc': '21/02/1996', 'CPF': '80350009188', 'Titulo_Eleitor': '718729793831'},
{'Nome': 'Manuella da Mata', 'Data_Nasc': '17/10/2002', 'CPF': '94632930355', 'Titulo_Eleitor': '343040882182'},
{'Nome': 'Calebe Rezende', 'Data_Nasc': '25/02/2004', 'CPF': '61175401322', 'Titulo_Eleitor': '993436801081'},
{'Nome': 'Diogo Almeida', 'Data_Nasc': '08/02/2001', 'CPF': '54194277299', 'Titulo_Eleitor': '641851806505'},
{'Nome': 'Bento Oliveira', 'Data_Nasc': '25/03/1998', 'CPF': '37805924877', 'Titulo_Eleitor': '170519413306'},
{'Nome': 'Letícia Guerra', 'Data_Nasc': '09/11/2001', 'CPF': '13883199422', 'Titulo_Eleitor': '345226235413'},
{'Nome': 'Bruna Martins', 'Data_Nasc': '13/08/2002', 'CPF': '43104712500', 'Titulo_Eleitor': '305501352231'},
{'Nome': 'Caleb Correia', 'Data_Nasc': '24/05/2001', 'CPF': '29140654933', 'Titulo_Eleitor': '638453041943'},
{'Nome': 'Henry Gabriel Moura', 'Data_Nasc': '26/11/1994', 'CPF': '71903167366', 'Titulo_Eleitor': '360202318572'},
{'Nome': 'João Miguel Martins', 'Data_Nasc': '20/07/1996', 'CPF': '77049746611', 'Titulo_Eleitor': '734873961710'},
{'Nome': 'Daniel Duarte', 'Data_Nasc': '08/04/1995', 'CPF': '20881953866', 'Titulo_Eleitor': '177065652263'},
{'Nome': 'Pedro Miguel Siqueira', 'Data_Nasc': '07/07/2006', 'CPF': '47222594299', 'Titulo_Eleitor': '910121228496'},
{'Nome': 'Brenda Nascimento', 'Data_Nasc': '05/04/2003', 'CPF': '87768238655', 'Titulo_Eleitor': '401188724401'},
{'Nome': 'Nicole Montenegro', 'Data_Nasc': '23/08/2004', 'CPF': '72868549411', 'Titulo_Eleitor': '170448735240'},
{'Nome': 'Olívia Vargas', 'Data_Nasc': '19/11/2005', 'CPF': '44640283066', 'Titulo_Eleitor': '12762452314'},
{'Nome': 'Dom Oliveira', 'Data_Nasc': '21/06/1995', 'CPF': '99677773033', 'Titulo_Eleitor': '993492530392'},
{'Nome': 'Murilo Sales', 'Data_Nasc': '08/04/2001', 'CPF': '28481495588', 'Titulo_Eleitor': '120228510456'},
{'Nome': 'Aurora Pires', 'Data_Nasc': '13/11/1999', 'CPF': '72090639355', 'Titulo_Eleitor': '973603893671'},
{'Nome': 'Maria Isis Cardoso', 'Data_Nasc': '22/04/2000', 'CPF': '35122003899', 'Titulo_Eleitor': '758353853135'},
{'Nome': 'Kaique Gonçalves', 'Data_Nasc': '18/07/2001', 'CPF': '34245198399', 'Titulo_Eleitor': '565629153235'},
{'Nome': 'Maya da Cruz', 'Data_Nasc': '03/06/2002', 'CPF': '50583617955', 'Titulo_Eleitor': '282990483051'},
{'Nome': 'Ayla Novais', 'Data_Nasc': '29/11/1997', 'CPF': '98004875811', 'Titulo_Eleitor': '515924525533'},
{'Nome': 'Alana Lopes', 'Data_Nasc': '03/05/2006', 'CPF': '86328932466', 'Titulo_Eleitor': '549922095489'},
{'Nome': 'Asafe Marques', 'Data_Nasc': '30/03/1996', 'CPF': '22429459633', 'Titulo_Eleitor': '283220462894'},
{'Nome': 'Ana Vitória Aragão', 'Data_Nasc': '04/06/2004', 'CPF': '40298530722', 'Titulo_Eleitor': '143805762096'},
{'Nome': 'Alícia Guerra', 'Data_Nasc': '09/04/1996', 'CPF': '47953455388', 'Titulo_Eleitor': '599626255903'},
{'Nome': 'Maria Mendes', 'Data_Nasc': '08/11/1994', 'CPF': '90929311522', 'Titulo_Eleitor': '550625161532'},
{'Nome': 'Ravi Rios', 'Data_Nasc': '08/04/2001', 'CPF': '59257039011', 'Titulo_Eleitor': '994368907756'},
{'Nome': 'Henry Gabriel Garcia', 'Data_Nasc': '23/08/1997', 'CPF': '39133075833', 'Titulo_Eleitor': '138422517781'}
]

# Lsita de dicionários com as informações dos candidatos
# Lista de candidatos a prefeito com números fixos
candidatos_prefeito = [
    {"Número": '12', "Nome": "Carlos Silva", "Partido": "Partido da União", "Lema": "União e Progresso"},
    {"Número": '23', "Nome": "Ana Pereira", "Partido": "Partido Verde", "Lema": "Por um futuro sustentável"},
    {"Número": '34', "Nome": "João Souza", "Partido": "Partido da Liberdade", "Lema": "Liberdade para todos"},
    {"Número": '45', "Nome": "Mariana Lopes", "Partido": "Partido Social", "Lema": "Socialismo e Justiça"},
    {"Número": '56', "Nome": "Ricardo Santos", "Partido": "Partido Trabalhista", "Lema": "Trabalho e Dignidade"},
    {"Número": '67', "Nome": "Luciana Almeida", "Partido": "Partido Progressista", "Lema": "Progresso e Inovação"},
    {"Número": '78', "Nome": "Fernando Costa", "Partido": "Partido Democrático", "Lema": "Democracia e Igualdade"}
]

# Lista de candidatos a vereador com números fixos
candidatos_vereador = [
    {"Número": '10001', "Nome": "Beatriz Moura", "Partido": "Partido da União", "Lema": "União e Progresso"},
    {"Número": '10002', "Nome": "Pedro Henrique", "Partido": "Partido Verde", "Lema": "Por um futuro sustentável"},
    {"Número": '10003', "Nome": "Juliana Oliveira", "Partido": "Partido da Liberdade", "Lema": "Liberdade para todos"},
    {"Número": '10004', "Nome": "Felipe Gonçalves", "Partido": "Partido Social", "Lema": "Socialismo e Justiça"},
    {"Número": '10005', "Nome": "Camila Rocha", "Partido": "Partido Trabalhista", "Lema": "Trabalho e Dignidade"},
    {"Número": '10006', "Nome": "Rafael Martins", "Partido": "Partido Progressista", "Lema": "Progresso e Inovação"},
    {"Número": '10007', "Nome": "Gabriela Lima", "Partido": "Partido Democrático", "Lema": "Democracia e Igualdade"},
    {"Número": '10008', "Nome": "Lucas Ferreira", "Partido": "Partido da União", "Lema": "União e Progresso"},
    {"Número": '10009', "Nome": "Fernanda Alves", "Partido": "Partido Verde", "Lema": "Por um futuro sustentável"},
    {"Número": '10010', "Nome": "Daniel Costa", "Partido": "Partido da Liberdade", "Lema": "Liberdade para todos"},
    {"Número": '10011', "Nome": "Isabela Teixeira", "Partido": "Partido Social", "Lema": "Socialismo e Justiça"},
    {"Número": '10012', "Nome": "Vinícius Ramos", "Partido": "Partido Trabalhista", "Lema": "Trabalho e Dignidade"},
    {"Número": '10013', "Nome": "Larissa Carvalho", "Partido": "Partido Progressista", "Lema": "Progresso e Inovação"},
    {"Número": '10014', "Nome": "Thiago Nascimento", "Partido": "Partido Democrático", "Lema": "Democracia e Igualdade"},
    {"Número": '10015', "Nome": "Paula Ribeiro", "Partido": "Partido da União", "Lema": "União e Progresso"}
]

# Lista de dicionários para armazenar o nome e a quantidade de votos do candidato
# Aqui também será exibido os votos brancos e nulos
votos_candidatos = [{"Número": '12', "Nome": "Carlos Silva", "Voto": [0]},
    {"Número": '23', "Nome": "Ana Pereira", "Voto": [0]},
    {"Número": '34', "Nome": "João Souza", "Voto": [0]},
    {"Número": '45', "Nome": "Mariana Lopes", "Voto": [0]},
    {"Número": '56', "Nome": "Ricardo Santos", "Voto": [0]},
    {"Número": '67', "Nome": "Luciana Almeida", "Voto": [0]},
    {"Número": '78', "Nome": "Fernando Costa", "Voto": [0]},
    {"Número": '10001', "Nome": "Beatriz Moura", "Voto": [0]},
    {"Número": '10002', "Nome": "Pedro Henrique", "Voto": [0]},
    {"Número": '10003', "Nome": "Juliana Oliveira", "Voto": [0]},
    {"Número": '10004', "Nome": "Felipe Gonçalves", "Voto": [0]},
    {"Número": '10005', "Nome": "Camila Rocha", "Voto": [0]},
    {"Número": '10006', "Nome": "Rafael Martins", "Voto": [0]},
    {"Número": '10007', "Nome": "Gabriela Lima", "Voto": [0]},
    {"Número": '10008', "Nome": "Lucas Ferreira", "Voto": [0]},
    {"Número": '10009', "Nome": "Fernanda Alves", "Voto": [0]},
    {"Número": '10010', "Nome": "Daniel Costa", "Voto": [0]},
    {"Número": '10011', "Nome": "Isabela Teixeira", "Voto": [0]},
    {"Número": '10012', "Nome": "Vinícius Ramos", "Voto": [0]},
    {"Número": '10013', "Nome": "Larissa Carvalho", "Voto": [0]},
    {"Número": '10014', "Nome": "Thiago Nascimento", "Voto": [0]},
    {"Número": '10015', "Nome": "Paula Ribeiro", "Voto": [0]},
    {"Número": '00000', "Nome": "Votos Brancos", "Voto": [0]}
]

# Lista de dicionários para armazenar o nome do partido e a quantidade de votos por partido
votos_por_partido = []

# Lista de dicionários para armazenar as infromações dos mesários e emitir a declaração de comparecimento
mesarios = []

# Lista de dicionários para armazenar os eleitores que já votaram
eleitores_que_votaram = []

# 3° Seção - Funções

# def para localizar informações no banco de dados
def localizar(dicionarios, localizacao):
    for indice, informacao in enumerate(dicionarios):
        for valor in informacao.values():
            if isinstance(valor, str) and localizacao.lower() == valor.lower():
                return indice
    return -1

def teste_teclado():
   print("\n------------------ URNA ELETRÔNICA ------------------\n----------------- TESTE DO TECLADO ------------------")
   for i in range(10):
      while True:
        try:
          teclado = int(input(f"Aperte a tecla {i}: "))
          if teclado == i:
            break
          else:
            print("Incorreto. Tente novamente!")
        except ValueError:
          print("\nERRO!\nValor Não Reconhecido!\n")
      
# 4° Seção - Váriaveis

# Menu principal para vizualização somente dos mesários, referente a votação
menu_principal = """------------------ URNA ELETRÔNICA -------------------

1 - Iniciar Voto
2 - Encerrar Seção
3 - Configurações
"""
# Menu de configuração exibido somente para os mesários, para cadastrar/alterar eleitores, candidatos, partidos, zerar urna
menu_configuracao = """------------------- CONFIGURAÇÕES --------------------

1 - Resetar Urna
2 - Exibir Opções de Eleitores
3 - Exibir Opções de Candidatos
4 - Voltar

------------------- ELEIÇÕES - 2024 -------------------
"""
# Menu comum a todos, confirmação, anular
menu_comum = """--------- ELEITOR DIGITE UMA DAS APÇÕES ABAIXO --------

1 - Confirmar
2 - Corrigir

"""
# Menu pós voto, será exibido para o mesário confirmar a incersão do voto ou para reiniciar o vato
# Reiniciar (Esse caso é utilizado caso o elitor tenha dificuldade, ou tenha alguma situação atípica)
menu_pos_voto = """--------- MESÁRIO DIGITE UMA DAS APÇÕES ABAIXO --------

1 - Confirmar Voto do Eleitor
2 - Reiniciar Voto do Eleitor

------------------- ELEIÇÕES - 2024 -------------------
"""
# Menu para exibir opções de cadastro e exibição
menu_exibir = """----------------------- OPÇÔES ------------------------

1 - Vizualisar Todos
2 - Cadastrar
3 - Apagar Dados
4 - Voltar

------------------- ELEIÇÕES - 2024 -------------------
"""
# Menu para exibir opções de cadastro e exibição
menu_teste_teclado = """----------------- TESTES DO TECLADO -------------------

Este teste é necessário para verificar se todas 
as teclas estão funcionando corretamente

--------- Caso dê erro chame o suporte do TRE ---------

------------------- ELEIÇÕES - 2024 -------------------
"""

teste_do_teclado = 1
mesarios_cadastrados = 1
flag = 1

# 4° Seção - Códigos

while True:
    if teste_do_teclado == 1: 
      teste_teclado()
      teste_do_teclado -= 1
    elif teste_do_teclado == 0:
      if len(mesarios) != 2:
        print("\n------------- IDENTIFICAÇÃO DE MESÁRIOS --------------\n")
        for i in range(1,3):
          while True:
            try:
              mesario = input(f"Digite o Título ou CPF do {i}° Mesário: ")
              posicao = localizar(eleitores_da_secao, mesario)
              verificacao = localizar(mesarios, mesario)
              if verificacao == -1:
                if posicao != -1:
                  mesario_encontrado = eleitores_da_secao[posicao]
                  print(f"\nNome: {mesario_encontrado['Nome']}\nData de Nascimento: {mesario_encontrado['Data_Nasc']}\nCPF: {mesario_encontrado['CPF']}\nTítulo de Eleitor: {mesario_encontrado['Titulo_Eleitor']}")
                  confirmacao = input("\nAs informações do mesário acima estão corretas [S/N]? ")
                  if confirmacao.upper() == "S":
                    mesario = {'Nome':mesario_encontrado['Nome'], 'Data_Nasc':mesario_encontrado['Data_Nasc'], 'CPF':mesario_encontrado['CPF'], 'Titulo':mesario_encontrado['Titulo_Eleitor']}
                    mesarios.append(mesario)
                    print(f"O(A) mesário(a) {mesario_encontrado['Nome']} foi cadastrado com sucesso!\n")
                    break
              elif verificacao != -1:
                print("\nMesário já cadastrado.\nVerifique as informações ou entre em contato com o suporte do TRE\n")
              elif len(mesario) != 11 or len(mesario) != 12:
                print("\nERRO AO CADASTRAR MESÁRIO!\nVerifique as informações ou entre em contato com o suporte do TRE\n")
            except ValueError:
              print("\nERRO!\nValor Não Reconhecido!\n")
        print("\n------------------ ELEIÇÕES - 2024 -------------------\n")
        print("\n---------------------- ZEREZIMA ----------------------\n")
        print("\n---------------- Votos dos Candidatos ----------------")
        print(tabulate(votos_candidatos, headers="keys", tablefmt="grid"))
        print("\n---------------- Eleitores que Votaram ---------------\n")
        if eleitores_que_votaram == []:
          print(f"Nenhum Eleitor Registrado\n")
        else:
          print("\n"+tabulate(eleitores_que_votaram, headers="keys", tablefmt="grid")+"\n")
      else:
        print(menu_principal)
        opcao = int(input("Digite uma das opções acima: "))
        print("------------------- ELEIÇÕES - 2024 -------------------")
        match opcao:
          case 1:
            print("\n------------------- URNA ELETRÔNICA -------------------\n")
            while True:
              try:
                print(eleitores_que_votaram)
                eleitor = input("Digite o CPF ou Título do Eleitor: ")
                if len(eleitor) == 11 or len(eleitor) == 12:
                  verificacao_eleitor = localizar(eleitores_que_votaram, eleitor)
                  if verificacao_eleitor != -1:
                    eleitor_verificacao = eleitores_que_votaram[verificacao_eleitor]
                    cpf = eleitor_verificacao['CPF']
                    titulo = eleitor_verificacao['Titulo']
                    if cpf == eleitor or titulo == eleitor:
                      print(f"\nO eleitor(a) {eleitor_verificacao['Nome']} já votou. Verifique as informações ou entre em contato com o TRE\n")
                  else:
                    posicao = localizar(eleitores_da_secao, eleitor)
                    if posicao != -1:
                      eleitor_encontrado = eleitores_da_secao[posicao]
                      print(f"\nNome: {eleitor_encontrado['Nome']}\nData de Nascimento: {eleitor_encontrado['Data_Nasc']}\nCPF: {eleitor_encontrado['CPF']}\nTítulo de Eleitor: {eleitor_encontrado['Titulo_Eleitor']}")
                      confirmacao = input("\nAs infomações do eleitor acima estão corretas [S/N]: ")
                      if confirmacao.upper() == "S":
                        eleitor_voto = {'Nome':eleitor_encontrado['Nome'], 'Data_Nasc':eleitor_encontrado['Data_Nasc'], 'CPF':eleitor_encontrado['CPF'], 'Titulo':eleitor_encontrado['Titulo_Eleitor']}
                        eleitores_que_votaram.append(eleitor_voto)
                        while True:
                          print("\n------------------- URNA ELETRÔNICA -------------------\n----------------------- PREFEITO ----------------------\n")
                          voto = input("Digite o número do candidato ou 0 para votar em branco: ")
                          if len(voto) == 2:
                            posicao = localizar(candidatos_prefeito, voto)
                            if posicao != -1:
                              candidato_encontrado = candidatos_prefeito[posicao]
                              print(f"\nCandidato(a): {candidato_encontrado['Nome']}\nPartido: {candidato_encontrado['Partido']}\nLema: {candidato_encontrado['Lema']}\n")
                              confirmacao = int(input("As infomações do candidato acima estão corretas:\n1 - Confirmar\n2 - Corrigir\n -->> "))
                              match confirmacao:
                                case 1:
                                  posicao = localizar(votos_candidatos, voto)
                                  candidato_encontrado = votos_candidatos[posicao]
                                  candidato_encontrado['Voto'][0] += 1
                                  
                                  print(eleitor_voto)
                                  print("\nVOTO CONFIRMADO!\n")
                                  break
                                case 2:
                                  print("CORRIGIR!!!")
                          elif voto == '0':
                            posicao = localizar(votos_candidatos, "00000")
                            branco = votos_candidatos[posicao]
                            branco['Voto'][0] += 1
                            print("\nVOTO EM BRANCO CONFIRMADO!\n")
                            break
                          else:
                            print("\nERRO! TENTE NOVAMENTE!\n")
                        while True:
                          print("\n------------------ URNA ELETRÔNICA ------------------\n------------------ VEREADOR ------------------\n")
                          voto = input("Digite o número do candidato ou 0 para votar em branco: ")
                          if len(voto) == 2:
                            posicao = localizar(candidatos_prefeito, voto)
                            if posicao != -1:
                              candidato_encontrado = candidatos_prefeito[posicao]
                              print(f"\nCandidato(a): {candidato_encontrado['Nome']}\nPartido: {candidato_encontrado['Partido']}\nLema: {candidato_encontrado['Lema']}\n")
                              confirmacao = int(input("As infomações do candidato acima estão corretas:\n1 - Confirmar\n2 - Corrigir\n -->> "))
                              match confirmacao:
                                case 1:
                                  posicao = localizar(votos_candidatos, voto)
                                  candidato_encontrado = votos_candidatos[posicao]
                                  candidato_encontrado['Voto'][0] += 1
                                  eleitor_voto = {'Nome':eleitor_encontrado['Nome'], 'Data_Nasc':eleitor_encontrado['Data_Nasc'], 'CPF':eleitor_encontrado['CPF'], 'Titulo':eleitor_encontrado['Titulo_Eleitor']}
                                  eleitores_que_votaram.append(eleitor_voto)
                                  print("\nVOTO CONFIRMADO!\n")
                                  break
                                case 2:
                                  print("CORRIGIR!!!")
                          elif voto == '0':
                            posicao = localizar(votos_candidatos, "00000")
                            branco = votos_candidatos[posicao]
                            branco['Voto'][0] += 1
                            print("\nVOTO EM BRANCO CONFIRMADO!\n")
                            break
                          else:
                            print("\nERRO! TENTE NOVAMENTE!\n")
                    else:
                      print("\nEleitor não encontrado no banco de dados!\nVerifique as informações ou entre em contato com o suporte do TRE\n")
              except ValueError:
                print("\nERRO\nConsulta de Eleitor incorreta, verifique as informações!")
              break

                  
          case 2:
            print("Você digitou 2")
            print("\n"+tabulate(mesarios, headers="keys", tablefmt="grid")+"\n")
            print("\n"+tabulate(votos_candidatos, headers="keys", tablefmt="grid")+"\n")
            print("\n"+tabulate(eleitores_que_votaram, headers="keys", tablefmt="grid")+"\n")
            break
           
              # case 3:
              #   print("Você digitou 3")
              #   break
              # case 4:
              #   print("Você digitou 4")
              #   break

# Próxima atualização: 
# Bloquear para que o mesmo mesário não seja cadastrado 2 vezes, o mesmo para o eletor não votar duas vezes
# Logo após o cadastro dos mesários emitir as zerezimas
# Adicionar a seção de voto para vereadores

# Póxima atualização
# Inserir a tela de configurações, exigir uma senha de acesso, com número de tentativas se o usuário exceder o número de tentatitivas bloquear a urna
# Inserir todas as outras opções que estão no menu principal e nos outros menus
# Realizar a depuração dos votos e exibir os vencedores
# Exibir o horário de encerramento das eleições
# Emitir o BU - Boletim de Urna