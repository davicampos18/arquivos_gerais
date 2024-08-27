#Exercício 2

#Fazer um programa que recebe vários números, e quando for digitado um valor negativo, mostrar a média dos números digitados (não considerar o negativo)

#Começar com o while

soma = 0
quantidade = 0

while True:
  numero = float(input("Digite um número: "))
  if numero >= 0:
    soma =+ numero
    quantidade =+ 1
  else:
    break
    
media = soma / quantidade
print(f"A média dos números digitados é: {media}")