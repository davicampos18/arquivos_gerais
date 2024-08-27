#EXERCÍCIO DE N° 3
# Escreva um programa que leia números inteiros do usuário até que ele digite 0 (zero). Armazene os números em uma lista e imprima a lista na tela.

num1 = []

while True:
  num = int(input("Digite um número inteiro: "))

  if num == 0:
    break

  num1.append(num)

print("Lista de números digitado:")
for num in num1:
  print(num)