from datetime import datetime


eleitores_da_secao = [
{'Nome': 'Melissa Novaes', 'Data_Nasc': '01/08/2006', 'CPF': '65564388711', 'Titulo_Eleitor': '914162022138'},
{'Nome': 'Gustavo Henrique Macedo', 'Data_Nasc': '21/02/1996', 'CPF': '80350009188', 'Titulo_Eleitor': '718729793831'},
{'Nome': 'Manuella da Mata', 'Data_Nasc': '17/10/2002', 'CPF': '94632930355', 'Titulo_Eleitor': '343040882182'},
{'Nome': 'Calebe Rezende', 'Data_Nasc': '25/02/2004', 'CPF': '61175401322', 'Titulo_Eleitor': '993436801081'},
{'Nome': 'Diogo Almeida', 'Data_Nasc': '08/02/2001', 'CPF': '54194277299', 'Titulo_Eleitor': '641851806505'}
]

candidatos_prefeito = [
{"Número": '12', "Nome": "Carlos Silva", "Partido": "Partido da União", "Lema": "União e Progresso"},
{"Número": '23', "Nome": "Ana Pereira", "Partido": "Partido Verde", "Lema": "Por um futuro sustentável"},
{"Número": '34', "Nome": "João Souza", "Partido": "Partido da Liberdade", "Lema": "Liberdade para todos"},
{"Número": '45', "Nome": "Mariana Lopes", "Partido": "Partido Social", "Lema": "Socialismo e Justiça"},
{"Número": '13', "Nome": "Ricardo Santos", "Partido": "Partido Trabalhista", "Lema": "Trabalho e Dignidade"},
{"Número": '22', "Nome": "Luciana Almeida", "Partido": "Partido Progressista", "Lema": "Progresso e Inovação"},
{"Número": '78', "Nome": "Fernando Costa", "Partido": "Partido Democrático", "Lema": "Democracia e Igualdade"}
]

candidatos_vereador = [
{"Número": '12001', "Nome": "Beatriz Moura", "Partido": "Partido da União", "Lema": "União e Progresso"},
{"Número": '23002', "Nome": "Pedro Henrique", "Partido": "Partido Verde", "Lema": "Por um futuro sustentável"},
{"Número": '34003', "Nome": "Juliana Oliveira", "Partido": "Partido da Liberdade", "Lema": "Liberdade para todos"},
{"Número": '45004', "Nome": "Felipe Gonçalves", "Partido": "Partido Social", "Lema": "Socialismo e Justiça"},
{"Número": '13005', "Nome": "Camila Rocha", "Partido": "Partido Trabalhista", "Lema": "Trabalho e Dignidade"},
{"Número": '22006', "Nome": "Rafael Martins", "Partido": "Partido Cristão", "Lema": "Progresso e Inovação"},
{"Número": '78007', "Nome": "Gabriela Lima", "Partido": "Partido Democrático", "Lema": "Democracia e Igualdade"},
{"Número": '12008', "Nome": "Lucas Ferreira", "Partido": "Partido da União", "Lema": "União e Progresso"},
{"Número": '23009', "Nome": "Fernanda Alves", "Partido": "Partido Verde", "Lema": "Por um futuro sustentável"},
{"Número": '34010', "Nome": "Daniel Costa", "Partido": "Partido da Liberdade", "Lema": "Liberdade para todos"},
{"Número": '45011', "Nome": "Isabela Teixeira", "Partido": "Partido Social", "Lema": "Socialismo e Justiça"},
{"Número": '13012', "Nome": "Vinícius Ramos", "Partido": "Partido Trabalhista", "Lema": "Trabalho e Dignidade"},
{"Número": '22013', "Nome": "Larissa Carvalho", "Partido": "Partido Cristão", "Lema": "Progresso e Inovação"},
{"Número": '78014', "Nome": "Thiago Nascimento", "Partido": "Partido Democrático", "Lema": "Democracia e Igualdade"},
{"Número": '12015', "Nome": "Paula Ribeiro", "Partido": "Partido da União", "Lema": "União e Progresso"}
]

votos_candidatos = [
{"Número": '12', "Partido": "Partido da União", "Nome": "Carlos Silva", "Voto": [1]},
{"Número": '23', "Partido": "Partido Verde", "Nome": "Ana Pereira", "Voto": [0]},
{"Número": '34', "Partido": "Partido da Liberdade", "Nome": "João Souza", "Voto": [0]},
{"Número": '45', "Partido": "Partido Social", "Nome": "Mariana Lopes", "Voto": [0]},
{"Número": '13', "Partido": "Partido Trabalhista", "Nome": "Ricardo Santos", "Voto": [0]},
{"Número": '22', "Partido": "Partido Cristão", "Nome": "Luciana Almeida", "Voto": [0]},
{"Número": '78', "Partido": "Partido Democrático", "Nome": "Fernando Costa", "Voto": [0]},
{"Número": '12001', "Partido": "Partido da União", "Nome": "Beatriz Moura", "Voto": [0]},
{"Número": '23002', "Partido": "Partido Verde", "Nome": "Pedro Henrique", "Voto": [0]},
{"Número": '34003', "Partido": "Partido da Liberdade", "Nome": "Juliana Oliveira", "Voto": [0]},
{"Número": '45004', "Partido": "Partido Social", "Nome": "Felipe Gonçalves", "Voto": [1]},
{"Número": '13005', "Partido": "Partido Trabalhista", "Nome": "Camila Rocha", "Voto": [0]},
{"Número": '22006', "Partido": "Partido Cristão", "Nome": "Rafael Martins", "Voto": [0]},
{"Número": '78007', "Partido": "Partido Democrático", "Nome": "Gabriela Lima", "Voto": [0]},
{"Número": '12008', "Partido": "Partido da União", "Nome": "Lucas Ferreira", "Voto": [0]},
{"Número": '23009', "Partido": "Partido Verde", "Nome": "Fernanda Alves", "Voto": [0]},
{"Número": '34010', "Partido": "Partido da Liberdade", "Nome": "Daniel Costa", "Voto": [0]},
{"Número": '45011', "Partido": "Partido Social", "Nome": "Isabela Teixeira", "Voto": [0]},
{"Número": '13012', "Partido": "Partido Trabalhista", "Nome": "Vinícius Ramos", "Voto": [0]},
{"Número": '22013', "Partido": "Partido Cristão", "Nome": "Larissa Carvalho", "Voto": [0]},
{"Número": '78014', "Partido": "Partido Democrático", "Nome": "Thiago Nascimento", "Voto": [0]},
{"Número": '12015', "Partido": "Partido da União", "Nome": "Paula Ribeiro", "Voto": [0]},
{"Número": '00000', "Partido": "Branco", "Nome": "Votos Brancos", "Voto": [0]}
]

votos_por_partido = [
 {"Número": '12', "Partido": "Partido da União", "Voto": [1]},
 {"Número": '23', "Partido": "Partido Verde", "Voto": [1]},
 {"Número": '34', "Partido": "Partido da Liberdade", "Voto": [1]},
 {"Número": '45', "Partido": "Partido Social", "Voto": [1]},
 {"Número": '13', "Partido": "Partido Trabalhista", "Voto": [1]},
 {"Número": '22', "Partido": "Partido Cristão", "Voto": [0]},
 {"Número": '78', "Partido": "Partido Democrático", "Voto": [0]}
]

mesarios = []

eleitores_que_votaram = []


def localizar(dicionarios, localizacao):
    for indice, informacao in enumerate(dicionarios):
        for valor in informacao.values():
            if isinstance(valor, str) and localizacao.lower() == valor.lower():
                return indice
            elif isinstance(valor, dict) or isinstance(valor, list) and localizacao == valor:
                return indice
    return -1

def localizacao(dicionarios, localizacao):
    for indice, informacao in enumerate(dicionarios):
        for valor in informacao.values():
            if isinstance(valor, dict) or isinstance(valor, list) and localizacao == valor:
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

def maior_valor(banco_de_dados:list, chave_para_encontrar):
  valores = []
  for possivel_valor in banco_de_dados:
    for chave, valor in possivel_valor.items():
      if chave == chave_para_encontrar:
         valores.append(valor)
  valor_encontrado = max(valores)
  return valor_encontrado[0]

## Apuração Prefeito

prefeito_vencedor = []

def apuracao(banco_de_dados_limite_for=votos_candidatos, banco_de_dados_adição=prefeito_vencedor, banco_de_dados_encontrar_valor=votos_candidatos):
    for posicao in range(0, banco_de_dados_limite_for):
        dicionario_analise = banco_de_dados_encontrar_valor[posicao]
        if len(dicionario_analise["Número"]) == 2:
            lista = dicionario_analise["Voto"]
            valor_analise = lista[0]
            if valor_analise == maior_valor(banco_de_dados_encontrar_valor, "Voto"):
                banco_de_dados_adição.append(dicionario_analise)


#################### Apuração Vereador ################
total_de_candidatos = len(votos_candidatos)
vereadores_com_votos = []
cadeira_por_partido = []
cadeiras_na_camara = 5
quociente_eleitoral = (len(eleitores_da_secao) / cadeiras_na_camara)

def verificacao_votos_vereador(banco_de_dados_com_os_candidatos:list):
   for posicao_candidato in range(0, total_de_candidatos):
      candidato_encontrado = banco_de_dados_com_os_candidatos[posicao_candidato]
      if len(candidato_encontrado["Número"]) == 5:
         if candidato_encontrado["Voto"][0] != 0:
            vereadores_com_votos.append(candidato_encontrado)


def quantidade_de_cadeiras_por_partido(banco_de_dados_com_os_partidos:list):
   for posicao in range(0, len(banco_de_dados_com_os_partidos)):
      partido = banco_de_dados_com_os_partidos[posicao]
      votos = partido['Voto'][0]
      votos_numero = int(votos)
      quociente_partidario = int(votos_numero / quociente_eleitoral)
      cadeiras_do_partido = {
        "Partido":partido['Partido'],
        "Cadeiras":quociente_partidario,
        "Número":partido["Número"]
    }
      cadeira_por_partido.append(cadeiras_do_partido)
      continue
      

# def ocupantes_de_cadeiras_na_camara():
#    while True:
#       if cadeiras_na_camara == 0:
#          break
#       else:
         




# candidatos = votos_candidatos.copy()
# candidatos.pop(-1)
# partidos = cadeira_por_partido.copy()
# candidatos_do_partido = []
# candidatos_que_ocuparao_uma_cadeira = []
# quantidade_de_partidos = len(cadeira_por_partido)
# quantidade_de_candidatos = len(candidatos)

# if eleicao_encerrada == 0:
#     while True:
#         if cadeiras_na_camara == 0:
#             break
#         else:
#             for posicao_do_partido in range(0, quantidade_de_partidos):
#                 partido_em_analise = cadeira_por_partido[posicao_do_partido]
#                 if partido_em_analise["Cadeiras"] != 0:
#                     nome_do_partido = partido_em_analise["Partido"]
#                     while True:
#                         for posicao_candidato in range(0, quantidade_de_candidatos):
#                             if posicao_candidato == quantidade_de_candidatos:
#                                 break
#                             else:
#                                 candidato_em_analise = candidatos[posicao_candidato]
#                                 partido_do_candidato = candidato_em_analise["Partido"]
#                                 analise_tipo_candidato = candidato_em_analise["Número"]
#                                 if len(analise_tipo_candidato) > 2:
#                                     numero_do_candidato = analise_tipo_candidato[0] + analise_tipo_candidato[1]
#                                     if numero_do_candidato == partido_em_analise["Número"]:
#                                         if partido_do_candidato == nome_do_partido:
#                                             candidatos_do_partido.append(candidato_em_analise)
#                                             candidatos.remove(candidato_em_analise)
#                                             quantidade_de_candidatos = quantidade_de_candidatos - 1
#                         cadeiras_encontradas = partido_em_analise["Cadeiras"]
#                         if candidatos_do_partido != [] and cadeiras_encontradas != 0:
#                             if cadeiras_encontradas > 1:
#                                 for cadeira in range(0, cadeiras_encontradas):
#                                         maior_voto = maior_valor(candidatos_do_partido, "Voto")
#                                         maior_voto = [maior_voto]
#                                         indice = localizacao(candidatos_do_partido, maior_voto)
#                                         candidato_para_ocupar_a_cadeira = candidatos_do_partido[indice]
#                                         candidatos_que_ocuparao_uma_cadeira.append(candidato_para_ocupar_a_cadeira)
#                                         candidatos_do_partido.pop(indice)
#                                         cadeiras_na_camara = cadeiras_na_camara -1
#                                 break
#                             elif cadeiras_encontradas == 1:
#                                 maior_voto = maior_valor(candidatos_do_partido, "Voto")
#                                 maior_voto = [maior_voto]
#                                 indice = localizacao(candidatos_do_partido, maior_voto)
#                                 candidato_para_ocupar_a_cadeira = candidatos_do_partido[indice]
#                                 candidatos_que_ocuparao_uma_cadeira.append(candidato_para_ocupar_a_cadeira)
#                                 candidatos_do_partido.clear()
#                                 cadeiras_na_camara = cadeiras_na_camara -1
#                                 break
#                             else:
#                                 print("Erro ao localizar a cadeira")
#                         else:
#                             break
    
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


# Dicionários para traduzir os nomes de dias e meses manualmente
dias_semana = {
    0: "segunda-feira",
    1: "terça-feira",
    2: "quarta-feira",
    3: "quinta-feira",
    4: "sexta-feira",
    5: "sábado",
    6: "domingo"
}


meses = {
    1: "janeiro",
    2: "fevereiro",
    3: "março",
    4: "abril",
    5: "maio",
    6: "junho",
    7: "julho",
    8: "agosto",
    9: "setembro",
    10: "outubro",
    11: "novembro",
    12: "dezembro"
}


# Obter a data e hora atuais
data_atual = datetime.now()


# Formatar a data por extenso manualmente
dia_semana = dias_semana[data_atual.weekday()]  # weekday() retorna 0 para segunda e 6 para domingo
dia = data_atual.day
mes = meses[data_atual.month]
ano = data_atual.year


data_por_extenso = f"{dia_semana}, {dia} de {mes} de {ano}"


# Exibir a hora
hora_atual = data_atual.strftime('%H:%M')     