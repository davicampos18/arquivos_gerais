# Prova de n° 8
# Módulo PYIA - Python IA - Aula 5 | Funções II

"""[PYIA-A05] Crie uma função chamada maior_numero que receberá três números como argumentos.
Esta função deve comparar os três números e identificar qual deles é o maior.
Para isso, utilize uma estrutura de controle que verifique qual número é maior que os outros dois.
A função deve então retornar o maior número encontrado."""

def maior_numero(num1:float, num2:float, num3:float) -> float:
    """Descobrir o maior número dentre os números digitados
    """
    if num1 > num2 and num1 > num3:
      return num1
    elif num2 > num1 and num2 > num3:
       return num2
    elif num3 > num1 and num3 > num2:
       return num3
    
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

print(maior_numero(num1, num2, num3))


"""Mesma Função Ternário"""

# def maior_numero(num1:float, num2:float, num3:float) -> float:
#     """Descobrir o maior número dentre os números digitados
#     """
#     return num1 if num1 > num2 and num1 > num3 else (num2 if num2 > num3 else num3)

# num1 = float(input("Digite o primeiro número: "))
# num2 = float(input("Digite o segundo número: "))
# num3 = float(input("Digite o terceiro número: "))

# print(maior_numero(num1, num2, num3))

"""Mesma Função Simplificada"""

# def maior_numero(num1:float, num2:float, num3:float) -> float:
#     """Descobrir o maior número dentre os números digitados
#     """
#     return max(num1, num2, num3)

# print(maior_numero(num1, num2, num3))