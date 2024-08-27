#-> Dicionário 
#É uma coleção, NÂO É INDEXADA(Os valores não possuem posição númerica, mas é mutavel)
#Os valores inves de serem acessados por posição, são acessados por meio de chaves
#Não existe chave sem valor e virse versa
#Funcionam em forma de par CHAVE : VALOR
#SÃO REPRESENTASDOS POR {}

# dicionario = {"chave" : 'valor', 'nome' : 'Davi'}

# print(dicionario['nome'])

#Criem um dicionário que irá conter infgormações de um estado
#Nome
#População
#Região
#Cada registro desses é uma chave e deve estar acompanhado de um valor, exiba cada informação de um estado em um print diferente

# estado = {'estado':'Bahia', 'populacao':'14016906', 'regiao':'Nordeste'}

# print(estado['estado'])
# print(estado['populacao'])
# print(estado['regiao'])

# estado['estado'] = 'São Paulo'
# print(estado['estado'])

#crie um dicionario funcionario, requisitos:
#Nome
#Função
#Salário
#Alterar a função e o sálario do funcionário

# funcionario = {'Nome':'Davi', 'Funcao':'Analista Judiciário', 'Salario':'R$ 10.000,00'}

# funcionario['Funcao'] = 'Magistrado'
# funcionario['Salario'] = 'R$ 25.000,00'

# print(funcionario)

#Metodos

#Metodos são ações que manipulam ou retornam algo da coleção

# #Adicionar uma nova chave e um novo valor no final do dicionário
# dicionario = {"chave" : 'valor', 'nome' : 'Davi'}
# dicionario.update({'nova_chave':'novo_valor'})
# print(dicionario)

# #Remove do dicionário a chave e o valor, passando apenas como critério a chave
# dicionario.pop('nova_chave')
# print(dicionario)

#Crie um dicionário vazio {}, adiocionar pares de chave e valor utilizando o update 
#Valres Serão: Nome da empresa, quantidade de funcionarios e renda da empresa

# empresa = {}

# empresa.update({'nome':'Campos Enterprise','qut_funcionarios':'50','renda':'10.000.000,00'})

# print(empresa)

#dicionario = {"chave" : 'valor', 'nome' : 'Davi'}

# #Retorna somente as chaves do dicionário
# print(dicionario.keys())

# #Retorna somente os valores do dicionário
# print(dicionario.values())

# #Retorna chave e valor do dicionário
# print(dicionario.items())

# for chave, valor in dicionario.items():
#   print(chave, valor)



lista = []

for i in range(0,3):
  nome_pessoa = input("Digite o nome da pessoa: ")
  idade_pessoa = int(input("Digite a idade da pessoa: "))

  dicionario_pessoa = {'nome':nome_pessoa, 'idade':idade_pessoa}

  lista.append(dicionario_pessoa)

print(lista)