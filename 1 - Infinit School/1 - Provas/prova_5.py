# Prova de n° 5
# Módulo PYIA - Python IA - Aula 2 | Dicionários e Sets

# Crie um dicionário que irá armazenar informações de um contato, incluindo o nome, o telefone e o email. Peça ao usuário para fornecer esses dados, solicitando que ele insira o nome do contato, o número de telefone e o endereço de email. Após coletar todas as informações necessárias, exiba o conteúdo do dicionário, mostrando todas as informações do contato inserido pelo usuário.

# Primeiro: Criar um dicionário vazio para aramazenar as informações
banco_de_dados = {}

# Segundo: Solicitar ao usuário que digite nome, telefone e o e-mail do contato a ser adicionado ao dicionário
nome = input("Qual o nome do contato que deseja cadastrar? ")
telefone = input(f"Digite o número de telefone de {nome}: ")
email = input(f"Digite o endereço de e-mail de {nome}: ")

# Terceiro: Inserir as informações fornecidas pelo usuário no dicionário
banco_de_dados.update({'nome':nome, 'telefone':telefone, 'email':email})

# Quarto: Exibir o conteúdo do dicionário
print(banco_de_dados)