# Prova de n° 7
# Módulo PYIA - Python IA - Aula 4 | Funções I

"[PYIA-A04] Crie uma função chamada media que receberá três números como argumentos. Esta função deve calcular a média aritmética desses três números. Para fazer isso, some os três números e, em seguida, divida o resultado por três. Por fim, a função deve retornar o valor da média aritmética calculada."

# Primeiro: Criar uma função para receber 3 notas e calcular a média

def media(nota1, nota2, nota3):
  return (nota1 + nota2 + nota3) / 3

# Segundo: Solicitar ao usuário que digite as 3 notas para que a média seja calculada
print("Digite as notas abaixo para poder calcular a média\n")

nota1 = float(input("Digite a 1° nota: "))
nota2 = float(input("Digite a 2° nota: "))
nota3 = float(input("Digite a 3° nota: "))

# Terceiro: Chamar a função e exibir o resultado da média
print(f"\nA média das notas é: {media(nota1, nota2, nota3):.2f}")

"FIM DA PROVA, ABAIXO SÓ TEM OUTRAS FORMAS DE FAZER A MESMA COISA, SÓ QUE COM LISTA E ESTRUTURA DE REPETIÇÃO"


# Função opcional com lista e estrutura de repetição FOR

# Primeiro: Criar a função para calcular a média com base em uma lista, teremos só um parâmetro, (sum) soma todos os elementos e (len) conta quantos elementos tem adicionado na minha lista

def media1(notas):
  return sum(notas) / len(notas)

# Segundo: Criar a lista para aramazenar as notas
notas = []

# Terceiro: Para não ficar repetindo o input criar um loop para isso e depois armazenar o valor na lista
for i in range(1, 4):
  nota = float(input(f"Digite a {i}° nota: "))
  notas.append(nota)

# Quarto: Exibir a média das notas
print(f"\nA média das notas é: {media1(notas):.2f}")


# Função opcional com lista e estrutura de repetição WHILE

# Primeiro: Criar a função para calcular a média com base em uma lista, teremos só um parâmetro, (sum) soma todos os elementos e (len) conta quantos elementos tem adicionado na minha lista

def media2(notas):
  return sum(notas) / len(notas)

# Segunto: Criar minha lista de notas
notas = []

# Terceiro: Exibir uma mensagem de boas-vindas e algumas orientações 
print("------------------------ Bem-Vindo ao Nosso Sistema Para Calcular Médias ----------------------\n* Você pode adicionar infinitas notas\n* Caso deseje encerrar e vizualizar a média, é só digitar um número negativo EX.: -1, -2")

# Quarto: Solicitar ao usuário que digite nome da matéria
materia = input("\nPara continuarmos, digite o nome da matéria: ")

# Quinto: Criar um loop while true para que o usuário adicione infinitas notas
while True:

  # Sexto: Solicitar ao usuário que digite a nota
  nota = float(input("Digite a nota para calcular a média: "))

  # Sétimo: Criar uma estrutura condicional para verificar o que o usuário digitou

  # Oitavo: IF para verificar se o valor digitado se enquadra nos parâmetros de uma nota, se sim, adiciona essa nota na lista e exibe uma mensagem informando aou usuário que a nota foi adicionada
  if nota > 0:
    notas.append(nota)
    print("Nota Adicionada com Sucesso!\n")

  # Nono: ELIF para verificar se o valor digitado é menor que zero(negativo), se sim, ele exibirá a média e irá parar o loop
  elif nota < 0 and len(notas) != 0:
    print(f"\nA média das notas adicionadas para a matéria de {materia} é {media2(notas):.2f}")
    break

  # Décimo: ELIF caso o usuário digite um valor negativo e a lista esteja vazia, ele irá perguntar se o usuário quer continuar ou não
  elif len(notas) == 0:
    print("\nNenhuma nota adicionada. Digite 1 para encerrar ou 2 para continuar:")
    opcao = int(input("Opção Desejada: "))

    # Décimo Primeiro: MatchCase para verificar qual a opção escolhida pelo usuário
    match opcao:
      case 1:
        print("\nMuito obrigado por utilizar o nosso sistema. Estamos encerrando....")
        break
      case 2:
        print("\n")
        continue
  # Décimo Segundo: ELSE caso ocorra algum erro      
  else:
    print("ERRO! TENTE NOVAMENTE!")
    continue