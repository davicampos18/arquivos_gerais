# PYIA - Python IA | Aula 5 - Funções II

# # Atividade Prática 1

# "Crie um programa que solicita ao usuário que insira três notas e, em seguida, calcule a média dessas notas usando uma função. A função deve receber as três notas como argumentos e retornar a média. Por fim, o programa deve imprimir a média calculada."

# # Primeiro: Criar a função para calcular a média
# # sum = soma todos os elemntos de uma lista ou tupla
# # len = retorna o número de elementos que uma lista ou tupla possui

# def media(notas):
#   return sum(notas) / len(notas)

# # Segundo: Criar a lista para aramazenar as notas
# notas = []

# # Terceiro: Para não ficar repetindo o input criar um loop para isso e depois armazenar o valor na lista
# for i in range(1, 4):
#   nota = float(input(f"Digite a {i}° nota: "))
#   notas.append(nota)

# # Quarto: Exibir a média das notas
# print(f"\nA média das notas é: {media(notas):.2f}")

# Atividade Prática 2

"Crie um programa que define uma função calcular_area_retangulo que recebe dois argumentos, comprimento e largura de um retângulo, e retorna am área desse retângulo. Em seguida, o programa deve solicitar ao usuário que insira o comprimento e a largura e imprimir a área calculada."

def calcular_area_retangulo(comprimento, largura):
  return comprimento * largura

comprimento = float(input("Digite o comprimento do reatângulo: "))
largura = float(input("Digite a largura do reatângulo: "))

print(f"\nA área do retângulo é de {calcular_area_retangulo(comprimento, largura):.2f} m²")