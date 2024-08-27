# #Um tipo de valor que armazena valores - Conjunto
# # -> Lista
# #É um conjunto que armazena valores, é ordenada, é mutavel, é representada por []

# #Exemplo

# lista_de_nomes = ['Guilherme', 'Marcelino', 'Gabriel']
# print(lista_de_nomes)

# #Sempre que precisar acessar um valor especifico da lista, será pela posição dele
# print(lista_de_nomes[2])

# #Alterar um valor na lista
# lista_de_nomes[1] = 'Davi'
# print(lista_de_nomes)

# #EXERCÍCIO1

# #Crie uma lista com 3 comidas que você gosta, exiba o valor que está na posição 1 e altere o valor que está na posição 3

# lista_comida = ['Feijoada', 'Lasanha', 'Comida Baiana', 'Pizza']
# print(lista_comida[1])
# lista_comida[2] = 'Pizza'
# print(lista_comida)

# #Metodos são ações que manipulam algo, podem ser utilizados inumeras vezes
# #nome_da_lista.nome_do_metodo(argumento)
# #Adiciona um valor na última posição
# lista_comida.append('uva')
# print(lista_comida)

# #Metodo para adicionar um valor em outra posição
# lista_comida.insert(2,'Pastel')
# print(lista_comida)

# #Metodo para remover
# lista_comida.pop()
# print(lista_comida)

# #Metodo para remover pela posição
# lista_comida.pop(1)
# print(lista_comida)

# #Remover pelo valor(Nome real que está dentro da lista)
# lista_comida.remove('Pizza')
# print(lista_comida)

# #Exercício 2
# #Crie uma lista de notas e adicione 2 notas utilizando append, adicione 2 notas utilizando insert, remova 1 nota utilizando pop

# lista_de_notas = []

# nota1 = float(input("Digite a primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))

# lista_de_notas.append(nota1)
# lista_de_notas.append(nota2)

# print(lista_de_notas)

# nota3 = float(input("Digite a terceira nota: "))
# posicao1 = int(input("Qual posição você deseja adicionar essa nota? "))
# nota4 = float(input("Digite a quarta nota: "))
# posicao2 = int(input("Qual posição você deseja adicionar essa nota? "))

# lista_de_notas.insert(posicao1, nota3)
# lista_de_notas.insert(posicao2, nota4)

# print(lista_de_notas)

# remover = int(input("Qual nota você deseja remover: "))
# lista_de_notas.pop(remover)

# print(lista_de_notas)

# #Exercício 3
# #Crie uma lista de idades e adicione 3 idades dentro dela, percorra a lista, se o valor for maior que 18 exiba "maior de idade", se for menor exiba "menor de idade"

# idades = [22, 18, 16]

# for idade in idades:
#   if idade >= 18:
#     print("Maior de idade")
#   else:
#     print("Menor de idade")

# -> Tupla
#São ordenadas, imutaveis e representadas por ()

tupla_de_nome = ('Guilherme', 'Pedro', 'André')

print(tupla_de_nome[2])

#Tranformando tupla em lista para fazer alteração
transformacao = list(tupla_de_nome)

#Tranformar lista em tupla
voltar = tuple(transformacao)
