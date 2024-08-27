#Entrada / Silocitar ao usuário que digite dois números inteiros
num1 = int(input("Digite o primeiro número Inteiro: "))
num2 = int(input("Digite o segundo número Inteiro: "))

soma = 0

#Processamento e saída
if num1 < num2:
  for i in range(num1, num2+1):
    if i % 2 == 0 :
      soma += i
elif num1 > num2:
  for i in range(num2, num1+1):
    if i % 2 == 0:
      soma += i
elif num1 == num2 and num1 % 2 == 0:
  print(f"Você digitou o mesmo número nas duas opções, mas o número {num1} é par.")
elif num1 == num2 and num1 % 2 != 0:
  print(f"Você digitou o mesmo número nas duas opções, mas o número {num1} é impar.")
else:
  print("O valor digitado é inválido!")
if soma != 0:
  print(f"A soma dos números pares dentro do intervalo digitado é de {soma}")