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
{"Número": '12', "Partido": "Partido da União", "Nome": "Carlos Silva", "Voto": [5]},
{"Número": '23', "Partido": "Partido Verde", "Nome": "Ana Pereira", "Voto": [0]},
{"Número": '34', "Partido": "Partido da Liberdade", "Nome": "João Souza", "Voto": [5]},
{"Número": '45', "Partido": "Partido Social", "Nome": "Mariana Lopes", "Voto": [0]},
{"Número": '13', "Partido": "Partido Trabalhista", "Nome": "Ricardo Santos", "Voto": [0]},
{"Número": '22', "Partido": "Partido Cristão", "Nome": "Luciana Almeida", "Voto": [0]},
{"Número": '78', "Partido": "Partido Democrático", "Nome": "Fernando Costa", "Voto": [0]},
{"Número": '12001', "Partido": "Partido da União", "Nome": "Beatriz Moura", "Voto": [0]},
{"Número": '23002', "Partido": "Partido Verde", "Nome": "Pedro Henrique", "Voto": [0]},
{"Número": '34003', "Partido": "Partido da Liberdade", "Nome": "Juliana Oliveira", "Voto": [0]},
{"Número": '45004', "Partido": "Partido Social", "Nome": "Felipe Gonçalves", "Voto": [0]},
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
 {"Número": '23', "Partido": "Partido Verde", "Voto": [3]},
 {"Número": '34', "Partido": "Partido da Liberdade", "Voto": [1]},
 {"Número": '45', "Partido": "Partido Social", "Voto": [2]},
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

prefeitos = []
candidato_a_prefeito_vencedor = []
candidatos_segundo_turno = []
votos = []
quantidade_de_vencedores = []

def apuracao_prefito():
    for prefeito_candidato in votos_candidatos:
      if len(prefeito_candidato["Número"]) == 2:
        prefeitos.append(prefeito_candidato)
        votos.append(prefeito_candidato["Voto"][0])
    maior_voto_prefeito = max(votos)
    for analise_voto in votos:
      if analise_voto == maior_voto_prefeito:
         quantidade_de_vencedores.append(analise_voto)
    if len(quantidade_de_vencedores) == 1:
      localizar_voto = [maior_voto_prefeito]
      localizacao_prefeito = localizacao(prefeitos, localizar_voto)
      prefeito_vencedor = prefeitos[localizacao_prefeito]
      candidato_a_prefeito_vencedor.append(prefeito_vencedor)
    elif len(quantidade_de_vencedores) > 1:
       for candidato in prefeitos:
          analise_voto_candidato = candidato["Voto"][0]
          if analise_voto_candidato == maior_voto_prefeito:
             candidatos_segundo_turno.append(candidato)

total_de_candidatos = len(votos_candidatos)
vereadores_com_votos = []
cadeira_por_partido = []
cadeiras_na_camara = 7
quociente_eleitoral = len(eleitores_da_secao) / cadeiras_na_camara

def verificacao_votos_vereador(banco_de_dados_com_os_candidatos:list):
    for posicao_candidato in range(total_de_candidatos):
        candidato_encontrado = banco_de_dados_com_os_candidatos[posicao_candidato]
        if len(candidato_encontrado["Número"]) == 5:
            if candidato_encontrado["Voto"][0] != 0:
                vereadores_com_votos.append(candidato_encontrado)

def quantidade_de_cadeiras_por_partido(banco_de_dados_com_os_partidos:list):
    for partido in banco_de_dados_com_os_partidos:
        votos = int(partido['Voto'][0])
        quociente_partidario = int(votos / quociente_eleitoral)
        cadeira_por_partido.append({
            "Partido": partido['Partido'],
            "Cadeiras": quociente_partidario,
            "Número": partido["Número"]
        })

candidatos_que_ocuparao_uma_cadeira = []
vereadores = []
candidatos_do_partido = []
cadeiras_a_serem_ocupadas = 7


def apuracao_vereadores():
  quantidade_de_cadeiras_por_partido(votos_por_partido)
  for i in range(0, len(votos_candidatos)):
    candidato = votos_candidatos[i]
    e_vereador = candidato["Número"]
    if len(e_vereador) == 5 and e_vereador != "00000":
      vereadores.append(candidato)
    else:
      continue

  while cadeiras_a_serem_ocupadas > 0:
    candidatos_do_partido.clear()
    for partido_em_analise in cadeira_por_partido:
        cadeiras_do_partido = partido_em_analise["Cadeiras"]
        print(candidatos_do_partido)
        print(cadeiras_do_partido)
        if cadeiras_do_partido >= 1:
          nome_do_partido = partido_em_analise["Partido"]
          for inserir_candidato in vereadores:
            if inserir_candidato["Partido"] == nome_do_partido:
              candidatos_do_partido.append(inserir_candidato)
          while cadeiras_do_partido > 0:
            candidato_com_maior_voto = maior_valor(candidatos_do_partido, "Voto")
            localizar_voto = [candidato_com_maior_voto]
            for anlise_candidato in candidatos_do_partido:
              if anlise_candidato["Voto"] == localizar_voto:
                candidatos_que_ocuparao_uma_cadeira.append(anlise_candidato)
                cadeiras_a_serem_ocupadas =- 1
                cadeiras_do_partido =- 1
                candidatos_do_partido.remove(anlise_candidato)
            if cadeiras_do_partido == 0:
              candidatos_do_partido.clear()
        else:
          continue
    
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