# Prova de n° 6
# Módulo PYIA - Python IA - Aula 3 | Revisão lógica de programação

"[PYIA-A03] Crie um dicionário para armazenar o nome e o preço de cinco produtos. Peça ao usuário para inserir o nome de cada produto e o respectivo preço. À medida que o usuário fornece os dados, armazene cada produto como uma chave no dicionário e o preço como o valor associado a essa chave. Após a inserção de todos os produtos e preços, calcule o valor total da compra somando todos os preços armazenados no dicionário. Por fim, exiba o valor total da compra."

# Primeiro: Criar um dicionário para armazenar os 5 produtos 
banco_de_dados = {}
# Segundo: Criar uma flag para armazenar os valores que serão somados
soma = 0

# Terceiro: Criar um loop para solicitar as informações ao usuário
for i in range(5):
  # Solicitar ao usuário que digite o nome do produto e o valor
  nome = input("Por gentileza, digite o nome do produto: ")
  preco = float(input(f"Agora digite o preço do produto {nome}: "))

  # Inserir as informações solicitadas ao usuário no dicionário chave = nome e o valor = preço 
  banco_de_dados.update({nome:preco})
  print("\n")

# Quarto: Criar um loop para percorrer co dicionário e somar os valores na flaf
for chave, valor in banco_de_dados.items():
  soma += valor

# Quinto: Exibir a soma de todos os produtos
print(f"\nO valor total da compra é de: R$ {soma:.2f}")