#Exercício 4

#Fazer um para idenficar se o número é primo ou não

#solicitação ao usuário
num = int(input("Digite um número: "))

#Processamento e Saída
if num % 2 == 0:
  print(f"{num} é um número primo.")

else:
  print(f"{num} não é um número primo.")