# PYIA - Python IA | Aula 4 - Funções I

# # Atividade 1 
# #Crie uma função que receba um nome e imprima uma saudação personalizada.

# def saudacao(nome):
#   return f"Olá, {nome}"

# print(saudacao("Davi"))

# # Atividade 2

# # Crie uam função que receba um horário e imprima "Bom dia!, Boa Tarde! Boa Noite!" Conforme o horário, somente números inteiros no formato 24h
# # Cuidado para não deixar a função simple demais e cabar retornando um valor inválido

# def horario(horas:int)->str:
#   if horas >= 5 and horas <= 11:
#     return "Bom dia!"
#   elif horas >= 12 and horas <= 17:
#     return "Boa tarde!"
#   elif horas >= 18 and horas <= 23:
#     return "Boa noite!"
#   elif horas >= 0 and horas <= 4:
#     return "Já é madrugada, você deveria estar dormindo"
#   else:
#     return "Hora Inválida!!!!"

# horas = int(input("Por gentileza, digite as horas (No formato 24h, e sem os minutos): "))

# print(horario(horas))

# # Atividade 3
# # Criar uma função que 2 números e mostre a soma dele

# def soma1(num1:float, num2:float)->float:
#   result = num1 + num2
#   return result

# num1 = float(input("Digite o primeiro número: "))
# num2 = float(input("Digite o segundo número: "))

# print(soma1(num1,num2))

# # Atividade 4
# # Criar uma função que receba 2 números e subtraia o primeiro pelo segundo

# def subtracao1(num1:float, num2:float)->float:
#   result = num1 - num2
#   return result

# num1 = float(input("Digite o primeiro número: "))
# num1 = float(input("Digite o segundo número: "))

# print(subtracao1(num1,num2))

# Atividade 5

# Crie uma calculadora com opções de soma, mutiplicação, subtração, divisão e sair.
# (Ela deverá funcionar infinitamente, até que o usuário decida sair da calculadora.)
# Utilize funções de rotina para cada operação e funções de unidade lógica para realizar os cálculos.

# Dica:
# Utilize de condicionais e laços de repetição para realizar esse exercício.


# def soma(num1:float, num2:float)->float:
#   result = num1 + num2
#   return result

# def subtracao(num1:float, num2:float)->float:
#   result = num1 - num2
#   return result

# def mutiplicacao(num1:float, num2:float)->float:
#   result = num1 * num2
#   return result

# def divisao(num1:float, num2:float)->float:
#   result = num1 / num2
#   return result

# while True:
#   print("================================ CÁLCULADORA ================================")
#   print("\n1 - Soma\n2 - Subtração\n3 - Divisão\n4 - Multiplicação\n5 - Sair\n")
#   opcao = int(input("ESCOLHA UMA DAS OPÇÕES ACIMA PARA REALIZAR A OPERAÇÃO(Apenas números): "))

#   match opcao:
#     case 1:
#       num1 = float(input("\nDigite o primeiro número para realizar a operação: "))
#       num2 = float(input("Digite o segundo número para realizar a operação: "))
#       print(f"{num1} + {num2} = {soma(num1,num2)}\n")
#     case 2:
#       num1 = float(input("\nDigite o primeiro número para realizar a operação: "))
#       num2 = float(input("Digite o segundo número para realizar a operação: "))
#       print(f"{num1} - {num2} = {subtracao(num1,num2)}\n")
#     case 3:
#       num1 = float(input("\nDigite o primeiro número para realizar a operação: "))
#       num2 = float(input("Digite o segundo número para realizar a operação: "))
#       print(f"{num1} / {num2} = {divisao(num1,num2)}\n")
#     case 4:
#       num1 = float(input("\nDigite o primeiro número para realizar a operação: "))
#       num2 = float(input("Digite o segundo número para realizar a operação: "))
#       print(f"{num1} * {num2} = {mutiplicacao(num1,num2)}\n")
#     case 5:
#       pergunta = input("\nVocê escolheu a opção (Sair), Tem certeza disso [S/N]? ")
#       if pergunta.upper() == "S":
#         print("\nMuito obrigado por utilizar a nossa cálculadora!")
#         break
#       else:
#         continue


def enesima(n):
  for i in range(1,n+1):
    print("")
    for a in range(i):
      print(i, " ",end="")


enesima(16)