# PYIA - Python IA | Aula 03

# DESAFIO PRÁTICO
# Gerenciamento de Compras de Produtos
# Você foi contratado para desenvolver um programa simples para auxiliar em um processo de compra de produtos. O programa deve permitir ao usuário inserir o nome e o preço de vários produtos, perguntando se deseja continuar inserindo mais produtos após cada entrada. Ao final, o programa deve fornecer um resumo da compra,

# Incluindo:
# A) O total gasto na compra.
# B) A quantidade de produtos que custam mais de R$1000.
# C) O nome do produto mais barato. Desenvolva o programa em Python utilizando conceitos de entrada/saída de dados, condicionais e laços de repetição.


# Primeiro: Criar um dicionário para servir como banco de dados para armazenar o nome e o valor do produto
# Criar uma flag para contar os produtos que custam mais de 1000
# Criar outra flag para armazenar o total da compra

banco_de_dados = {}
acima_de_mil = 0
total = 0

# Segundo: Exibir uma mensagem de boas-vindas e informações sobre o programa
print("------------------ Bem vindo ao nosso caixa -------------------\n\nEste sistema serve para te auxiliar nos processos de compras de produtos. Você pode inserir quantos produtos quiser com seus respectivos valores.\n\nPara facilitar a incersão dos produtos você irá inseri-los sem pausa, mas caso não queira mais inserir produtos, digite -1. Se o sistema for interrompido, você receberá as seguintes informações:\n\n1 - O total gasto na compra;\n2 - A quantidade de produtos que custam mais de R$ 1.000,00;\n3 - O nome e o valor do produto mais barato.\n---------------------------------------------------------------")

# Quarto: Criar um loop while = true para rodar o sistema até que o usuário decida que não irá
# cadastrar mais nenhum produto.
while True:

  # Quinto: Solicitar ao usuário que digite o nome e o preço do produto
  nome_produto = input("\nPor gentileza, digite o nome do produto: ")

  # Sexto: Verificar o valor que o usuário digitou, se digitou -1 encerrar o loop, se não, continuar para adicionar o preço do produto
  if nome_produto == "-1":
    # Sétimo: Caso o usuário queira encerrar, exibir as informações mencionadas anteriormente
    print(f"\nTotal da compra: R$ {total:.2f}\nTotal de produtos que custam mais de R$ 1.000,00: {acima_de_mil}\nO produto mais barato foi: {nome_menor_valor}, que custa R$ {menor_valor:.2f}")
    break
  else:
    preco_produto = float(input(f"Por gentileza, digite o valor do produto {nome_produto}: "))
    if preco_produto > 1000:
       acima_de_mil += 1
    # Oitavo: Adicionar os valores no banco de dados
    banco_de_dados[nome_produto] = preco_produto

  # Nono: Verificar o menor valor que está no banco de dados
  menor_valor = min(banco_de_dados.values())

  # Décimo: loop for para percorrer o banco de dados para cálcular o tatotal e localizar o nome do produto de menor valor
  for chave, valor in banco_de_dados.items():
    total += valor
    if valor == menor_valor:
      nome_menor_valor = chave