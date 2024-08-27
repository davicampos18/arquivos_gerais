# EXERCÍCIO DE N° 2
# Escreva um programa que peça ao usuário um número inteiro e imprima a tabuada desse número, utilizando a estrutura 'while'

num = int(input("Digite um número inteiro para obter a tabuada: "))

while num <= 10:
  print(f"TABUADA DE MULTIPLICAÇÃO DO NÚMERO {num}")
  for i in range(0,11):
    result = num * i
    print(f"{num} * {i} = {result}" )

  print(f"\nTABUADA DE ADIÇÃO DO NÚMERO {num}")
  for i in range(0,11):
    result1 = num + i

    print(f"{num} + {i} = {result1}" )

  print(f"\nTABUADA DE SUBTRAÇÃO DO NÚMERO {num}")
  for i in range(0,11):
    result2 = num - i
    print(f"{num} - {i} = {result2}" )

  break