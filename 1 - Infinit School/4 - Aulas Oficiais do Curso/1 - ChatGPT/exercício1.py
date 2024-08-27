# Exercício 1

#Faça um programa que peça 4 notas de um aluno (utilizando estruturas de repetição) e mostre a média delas.

#Solicitar ao usuário que digite o nome do aluno
nome = input("Por gentileza, digite o nome do aluno: ")

#Estrura de repetição para solicitar ao usuário as notas
notas = 0

for i in range (1,5):
  nota = float(input(f"Digite a {i}° nota: "))
  notas =+ nota
media = notas / 4

print(f"A média das notas de {nome} é {media}.")