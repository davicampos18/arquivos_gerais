import random

#Gerar número aleatório entre 1 e 10
def gerarnumerosecreto():
  return random.randint(1, 10)

numerosecreto = gerarnumerosecreto()
tentativas = 0

while tentativas < 3:

  adivinhacao = int(input("Digite o número inteiro que estou pensando: "))
  tentativas += 1

  if adivinhacao == numerosecreto:
    print(f"Parabéns, você acertou! O número que eu estava pensando era exatemente {numerosecreto}.")
    break
  elif tentativas == 3:
    print(f"Você não conseguiu acertar. O número secreto era {numerosecreto}. Mais sorte na próxima vez.")
    break
  elif adivinhacao > numerosecreto:
    print(f"Tente um número menor que {adivinhacao}")
  elif adivinhacao < numerosecreto:
    print(f"Tente um número maior que {adivinhacao}")