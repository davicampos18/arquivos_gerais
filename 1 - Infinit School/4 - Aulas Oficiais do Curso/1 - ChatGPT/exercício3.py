#Exercício 3

#Fazer um programa para calcular o fatorial de um número

#Começar com o if e depois else com FOR

num = 2
fatorial = 0

numero = int(input("Digite um número: "))

if numero == 1 or numero == 0:
  fatorial = 1
else:
  for i in range(0, numero):
    if i == 1:
      fatorial = i ** num
    if numero > 1:
      fatorial = fatorial * (i +1)


print(f"O valor fatorial de {numero} é {fatorial}.")