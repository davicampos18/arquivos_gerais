# 1° Seção - Inportações


# Importar o tabulate para gerar uma grade na depuração de votos que irá conter o nome do candidato e a quantidade de votos
from tabulate import tabulate
from funcoes import *

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
                          if len(voto) == 5:
                            posicao = localizar(candidatos_vereador, voto)
                            if posicao != -1:
                              candidato_encontrado = candidatos_vereador[posicao]
                              print(f"\nCandidato(a): {candidato_encontrado['Nome']}\nPartido: {candidato_encontrado['Partido']}\nLema: {candidato_encontrado['Lema']}\n")
                              confirmacao = int(input("As infomações do candidato acima estão corretas:\n1 - Confirmar\n2 - Corrigir\n -->> "))
                              match confirmacao:
                                case 1:
                                  posicao = localizar(votos_candidatos, voto)
                                  candidato_encontrado = votos_candidatos[posicao]
                                  candidato_encontrado['Voto'][0] += 1
                                  eleitor_voto = {'Nome':eleitor_encontrado['Nome'], 'Data_Nasc':eleitor_encontrado['Data_Nasc'], 'CPF':eleitor_encontrado['CPF'], 'Titulo':eleitor_encontrado['Titulo_Eleitor']}
                                  eleitores_que_votaram.append(eleitor_voto)
                                  posicao = localizar(votos_por_partido, candidato_encontrado['Partido'])
                                  partido_encontrado = votos_por_partido[posicao]
                                  partido_encontrado['Voto'][0] += 1
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
            apuracao_prefito()
            apuracao_vereadores()
            if len(quantidade_de_vencedores) > 1:
              print("\nNesta eleição teremos 2° turno para a prefeitura de Salvador, segue lista de candidatos")
              print(tabulate(candidatos_segundo_turno, headers="keys", tablefmt="grid"))
            else:
              informacao_candidato = candidato_a_prefeito_vencedor[0]
              print(f"\nO candidato vencedor a ocupar o cargo de prefeito da cidade de Salvador é {informacao_candidato["Nome"]} do partido {informacao_candidato["Partido"]} vencendo com {informacao_candidato["Voto"][0]}.")
            print("\nConfira abaixo os candidatos que ocuparão uma cadeira na câmara de vereadores:\n")
            print(tabulate(candidatos_que_ocuparao_uma_cadeira, headers="keys", tablefmt="grid"))

   
            print(f"""\n
------| ESTE DOCUMENTO É VERDADERIRO E DOU FÉ |-------
      
->>>>>>>>>>>>>> DAVI SILVA DE CAMPOS <<<<<<<<<<<<<<<<-     
     PRESIDENTE DO SUPERIOR TRIBUNAL ELEITORAL


         DOCUMENTO ASSINADO ELETRÔNICAMENTE
             CÓDIGO DE AUTENTICIDADE
         1E73YB3J1V323JN2C3BHJ2GNV2J3G1J32H
                  
    {data_por_extenso} às {hora_atual}


------------------- ELEIÇÕES - 2024 -------------------
""")
            break


           
          case 3:
            print("Você digitou 3")
            break


# Próxima atualização: 
# Bloquear para que o mesmo mesário não seja cadastrado 2 vezes, o mesmo para o eletor não votar duas vezes
# Logo após o cadastro dos mesários emitir as zerezimas
# Adicionar a seção de voto para vereadores


# Póxima atualização("Você digitou 3")

# Inserir a tela de configurações, exigir uma senha de acesso, com número de tentativas se o usuário exceder o número de tentatitivas bloquear a urna
# Inserir todas as outras opções que estão no menu principal e nos outros menus
# Realizar a depuração dos votos e exibir os vencedores
# Exibir o horário de encerramento das eleições
# Emitir o BU - Boletim de Urna