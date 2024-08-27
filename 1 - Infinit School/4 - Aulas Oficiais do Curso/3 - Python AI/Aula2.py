#Atividade prática 8 - da Aula 02 do módulo de PYIA - Python IA

#Escreva um programa que EXIBA um dicionário contendo informações de pessoas (nome, idade) e exiba essas informações.


dicionarios = [{'nome':'Davi', 'idade':'22'}, {'nome':"Alberto", "idade":"24"}]

for dicionario in (dicionarios):
  for chave, valor in dicionario.items():
    print(f"A chave é {chave} e o valor é {valor}")