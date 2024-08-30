# 1° Seção - Inportações

# Importar o tabulate para gerar uma grade na depuração de votos que irá conter o nome do candidato e a quantidade de votos
from tabulate import tabulate

# 2° Seção - Bancos de Dados
# Informações para cadastro de pessoas CPF, NOME, TÍTULO DE ELEITOR, DATA DE NASCIMENTO

# Lista de dicionários que contém as informações dos eleitores
eleitores_da_secao = []

# Lsita de dicionários com as informações dos candidatos
candidados = []

# Lista de dicionários para armazenar o nome e a quantidade de votos do candidato
# Aqui também será exibido os votos brancos e nulos
votos_candidatos = []

# Lista de dicionários para armazenar o nome do partido e a quantidade de votos por partido
votos_por_partido = []

# 3° Seção - Funções

# def para localizar informações no banco de dados
def localizar(dicionarios, localizacao):
  for indice, informacao in enumerate(dicionarios):
      if localizacao.lower() in [value.lower() for value in informacao.values()]:
          return indice
  return -1

# 4° Seção - Váriaveis

# Menu principal para vizualização somente dos mesários, referente a votação
menu_principal = """------------------ URNA ELETRÔNICA ------------------

1 - Iniciar Eleição
2 - Encerrar Seção
3 - Configurações

------------------ ELEIÇÕES - 2024 -------------------
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
3 - Branco

------------------- ELEIÇÕES - 2024 -------------------
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

# 4° Seção - Códigos

while True:
    if teste_do_teclado == 1:
        print(menu_teste_teclado)
        t0 = int(input("Aperte a tecla 0: "))
        if t0 == 0:
          t1 = int(input("Aperte a tecla 1: "))
          if t1 == 1:
              t2 = int(input("Aperte a tecla 2: "))
              if t2 == 2:
                  t3 = int(input("Aperte a tecla 3: "))
                  if t3 == 3:
                      t4 = int(input("Aperte a tecla 4: "))
                      if t4 == 4:
                          t5 = int(input("Aperte a tecla 5: "))
                          if t5 == 5:
                              t6 = int(input("Aperte a tecla 6: "))
                              if t6 == 6:
                                  t7 = int(input("Aperte a tecla 7: "))
                                  if t7 == 7:
                                      t8 = int(input("Aperte a tecla 8: "))
                                      if t8 == 8:
                                          t9 = int(input("Aperte a tecla 9: "))
                                          if t9 == 9:
                                            print("\nTeste do Teclado Concluído\n")
                                            teste_do_teclado -= 1
                                          else:
                                            print("\nVOCÊ DIGITOU A TECLA ERRADA, ESTAMOS REINICIANDO TESTE\n")
                                      else:
                                        print("\nVOCÊ DIGITOU A TECLA ERRADA, ESTAMOS REINICIANDO TESTE\n")    
                                  else:
                                    print("\nVOCÊ DIGITOU A TECLA ERRADA, ESTAMOS REINICIANDO TESTE\n")        
                              else:
                                print("\nVOCÊ DIGITOU A TECLA ERRADA, ESTAMOS REINICIANDO TESTE\n")            
                          else:
                            print("\nVOCÊ DIGITOU A TECLA ERRADA, ESTAMOS REINICIANDO TESTE\n")                
                      else:
                        print("\nVOCÊ DIGITOU A TECLA ERRADA, ESTAMOS REINICIANDO TESTE\n")                    
                  else:
                    print("\nVOCÊ DIGITOU A TECLA ERRADA, ESTAMOS REINICIANDO TESTE\n")                        
              else:
                print("\nVOCÊ DIGITOU A TECLA ERRADA, ESTAMOS REINICIANDO TESTE\n")
          else:
            print("\nVOCÊ DIGITOU A TECLA ERRADA, ESTAMOS REINICIANDO TESTE\n")
        else:
          print("\nVOCÊ DIGITOU A TECLA ERRADA, ESTAMOS REINICIANDO TESTE\n")
    else:
      if mesarios_cadastrados == 1:
          print("------------- IDENTIFICAÇÃO DE MESÁRIOS ---------------")
          mesario1 = int(input("Digite o Título ou CPF do 1° Mesário: "))
          posicao = localizar(eleitores_da_secao, mesario1)
          if posicao != -1:
            mesario_encontrado = eleitores_da_secao[posicao]
            print(f"\nNome: {mesario_encontrado['Nome']}\nData de Nascimento: {mesario_encontrado['Data_Nasc']}\nCPF: {mesario_encontrado['CPF']}\nTítulo de Eleitor: {mesario_encontrado['Titulo']}")
            confirmacao = input("As infommações do mesário acima estão corretar [S/N]: ")
            if confirmacao.upper() == "S":
              mesario2 = int(input("Digite o Título ou CPF do 2° Mesário: "))
              posicao = localizar(eleitores_da_secao, mesario2)
              if posicao != -1:
                mesario_encontrado = eleitores_da_secao[posicao]
                print(f"\nNome: {mesario_encontrado['Nome']}\nData de Nascimento: {mesario_encontrado['Data_Nasc']}\nCPF: {mesario_encontrado['CPF']}\nTítulo de Eleitor: {mesario_encontrado['Titulo']}")
                confirmacao = input("As infommações do mesário acima estão corretar [S/N]: ")
                if confirmacao.upper() == "S":
                  mesarios_cadastrados -= 1
                elif confirmacao.upper() == "N":
                   continue
              else:
                print("Mesário não encontrado, tente cadastrá-lo na seção ou verifique as informões.")
            elif confirmacao.upper() == "N":
              continue
          else:
              print("Mesário não encontrado, tente cadastrá-lo na seção ou verifique as informões.")
      else:
          print(menu_principal)
          opcao = int(input("\nDigite uma das opções acima: "))
          match opcao:
              case 1:
                print("Você digitou 1")
                break
              case 2:
                print("Você digitou 2")
                break
              case 3:
                print("Você digitou 3")
                break
              case 4:
                print("Você digitou 4")
                break