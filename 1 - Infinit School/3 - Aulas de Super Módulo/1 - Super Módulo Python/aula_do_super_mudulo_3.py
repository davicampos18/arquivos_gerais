# Aula de super módulo 3
# Funções

# É como se fosse uma mini-fábrica
# Função é um bloco de código pronto, que toda vez que seja necessário utilizá-lo basta chamar

# Para criar uma função (Definição de uma função)
# A quantidade de parametros a serem criados é infinito
# Parametros é quando constrói a função, argumentos é quando vai utilizá-la
# def nome_da_função(parametros)
# Se não tiver o return ela vai retornar NONE(Vazio)

# def soma(primeiro_numero, segundo_numero):
#   resultado = primeiro_numero + segundo_numero
#   return resultado

# print(soma(1,9))

# Não utilizar print ou input, isso quebra a identidade da função (Concelho do professor)

# def maior_idade(idade):
#   if idade >= 18:
#     return "Maior de Idade"
#   else:
#     return "Menor de Idade"

# idade = int(input("Digite sua idade: "))
# print(maior_idade(idade))

# Função sem parametro

# def saudacao():
#   return "Olá, mundo"

# print(saudacao())

# def saudacao(nome):
#   return f"Olá, {nome}"

# print(saudacao("Davi"))

# Atividade 1

# Crie uam função que receba um horário e imprima "Bom dia!, Boa Tarde! Boa Noite!" Conforme o horário, somente números inteiros no formato 24h

# Cuidado para não deixar a função simple demais e cabar retornando um valor inválido

# def horario(horas):
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

# Atividade 2 
# Criar uma função que 2 números e mostre a soma dele

# def soma_nao_gosto(num1, num2):
#   result = num1 + num2
#   return result

# num1 = float(input("Digite o primeiro número: "))
# num2 = float(input("Digite o segundo número: "))

# print(soma_nao_gosto(num1,num2))

# # Atividade 3
# # Criar uma função que receba 2 números e subtraia o primeiro pelo segundo

# def subtracao(num1, num2):
#   result = num1 - num2
#   return result

# num1 = float(input("Digite o primeiro número: "))
# num1 = float(input("Digite o segundo número: "))

# print(subtracao(num1,num2))

# Atividade 4

# Crie uma calculadora com opções de soma, mutiplicação, subtração, divisão e sair.
# (Ela deverá funcionar infinitamente, até que o usuário decida sair da calculadora.)
# Utilize funções de rotina para cada operação e funções de unidade lógica para realizar os cálculos.

# Dica:
# Utilize de condicionais e laços de repetição para realizar esse exercício.




def soma(num1, num2):
  result = num1 + num2
  return result

def subtracao(num1, num2):
  result = num1 - num2
  return result

def mutiplicacao(num1, num2):
  result = num1 * num2
  return result

def divisao(num1, num2):
  result = num1 / num2
  return result

while True:
  print("================================ CÁLCULADORA ================================")
  print("\n1 - Soma\n2 - Subtração\n3 - Divisão\n4 - Multiplicação\n5 - Sair\n")
  opcao = int(input("ESCOLHA UMA DAS OPÇÕES ACIMA PARA REALIZAR A OPERAÇÃO(Apenas números): "))

  match opcao:
    case 1:
      num1 = float(input("\nDigite o primeiro número para realizar a operação: "))
      num2 = float(input("Digite o segundo número para realizar a operação: "))
      print(f"{num1} + {num2} = {soma(num1,num2)}\n")
    case 2:
      num1 = float(input("\nDigite o primeiro número para realizar a operação: "))
      num2 = float(input("Digite o segundo número para realizar a operação: "))
      print(f"{num1} - {num2} = {subtracao(num1,num2)}\n")
    case 3:
      num1 = float(input("\nDigite o primeiro número para realizar a operação: "))
      num2 = float(input("Digite o segundo número para realizar a operação: "))
      print(f"{num1} / {num2} = {divisao(num1,num2)}\n")
    case 4:
      num1 = float(input("\nDigite o primeiro número para realizar a operação: "))
      num2 = float(input("Digite o segundo número para realizar a operação: "))
      print(f"{num1} * {num2} = {mutiplicacao(num1,num2)}\n")
    case 5:
      pergunta = input("\nVocê escolheu a opção (Sair), Tem certeza disso [S/N]? ")
      if pergunta.upper() == "S":
        print("\nMuito obrigado por utilizar a nossa cálculadora!")
        break
      else:
        continue