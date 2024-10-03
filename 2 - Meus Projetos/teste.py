def localizar(dicionarios, localizacao):
    for indice, informacao in enumerate(dicionarios):
        for valor in informacao.values():
            if isinstance(valor, str) and localizacao.lower() == valor.lower():
                return indice
            elif isinstance(valor, dict) and localizacao.lower() == valor:
               retu
    return -1

votos_candidatos = [{"Número": '12', "Nome": "Carlos Silva", "Voto": [0]},
    {"Número": '23', "Nome": "Ana Pereira", "Voto": [0]},
    {"Número": '34', "Nome": "João Souza", "Voto": [34]},
    {"Número": '45', "Nome": "Mariana Lopes", "Voto": [0]},
    {"Número": '56', "Nome": "Ricardo Santos", "Voto": [3]},
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

def apuracao(banco_de_dados:list):
  maior_voto = []
  for voto in banco_de_dados:
    for cahve, valor in voto.items():
      if cahve == "Voto":
        inserir = valor
        maior_voto.append(inserir)
  resultado = max(maior_voto)
  pesquisa = [resultado]
  posicao = localizar(votos_candidatos, pesquisa)
  vencedor = votos_candidatos[posicao]
  nome = vencedor["Nome"]
  numero = vencedor["Número"]
  votos = vencedor["Voto"]
  return f"{nome} com o número {numero}, venceu a eleição com {votos} votos"

print(apuracao())