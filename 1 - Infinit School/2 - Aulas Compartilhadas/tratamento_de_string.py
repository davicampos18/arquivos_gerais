# Aula Compartilhada | Strings

# # Usar o caracterer aspas

# problema = " usar aspas \' e aspas \"" # Escape

# # Concatenação de strings e f-string
# boa = "Boa"
# tarde = " tarde!"

# print(f"{boa}{tarde}")
# print("Boa" + " " + "tarde!")
# print("{:s}{:s}".format(boa, tarde))
# #print("a" + 1) erro
# print("a" + str(1)) # Converte para string
# print(f"a{1}")
# print("a{:d}".format(1)) # o "d" é de decimal

# # Cast = Mudança de tipo (Serve para qualquer linguagem de programação)

# # Indexed, Indexada ou Indexação

# cidade = 'Soterópolis'
# print(cidade[0]) # Vai imprimir o "S"
# print(cidade[1]) # Vai imprimir o "o"
# print("cachorro"[4]) # Vai imprimir o "o"
# print(cidade[-1]) # Sempre será o útimo caractere, ou seja, vai imprir o "s"

# # Fatiamento

# cidade = 'Soterópolis'

# # [0, 7] # Incluí o 0 e 7
# # ]0,7[ # Exclui o 0 e 7
# # [0,7[ # Incluí o 0 e exclui o 7

#  # print(cidade[INICIO_INCLUSIVO: FINAL_EXCLUSIVO: PASSO])
# print(cidade[0:6:1]) # Vai imprimir "Soteró"
# print(cidade[0:6:2]) # Vai imprimir "Str", porque está pulando de 2 em 2
# print(cidade[:6:1]) # Se começar da posição inicial, ou seja, 0
# print(cidade[2::1]) # Vai da posição em que coloquei, até  a final
# print(cidade[::]) # Vai imprimir tudo, se for de 1 em 1 pode ocultar em qualquer caso
# print(cidade[::-1]) # Inverte a string, vai imprimir "silopóretoS"

# # Strings - format

# x = 10
# y = 5
# z = -3

# print("ABC {:d} ABC".format(x)) # Vai imprimir "10"
# print("ABC {} ABC".format(x)) # Vai imprimir "10"
# print("ABC {0} {1} ABC".format(x, y)) # Vai imprimir "ABC 10 5 ABC"
# print("ABC {1} {0} ABC".format(x, y)) # Vai imprimir "ABC 5 10 ABC"
# print("ABC {1} {0} {1} ABC".format(x, y)) # Vai imprimir "ABC 5 10 5 ABC"
# print("{2}ABC {1} {0} {1} ABC".format(x, y, z)) # Vai imprimir "-3ABC 5 10 5 ABC"
# print("{x} ABC {a} ABC {d}".format(x="Davi", a="Fruta", d=10)) # Vai impromir "Davi ABC Fruta ABC 10"
# print("{:.2f}".format(2.26765286187356836)) # Arredondar para 2 casas decimais
# print("{:.2f}".format(2.26765286187356836 - .005)) # Arredondar para baixo
# print("{:.2f}".format(2.26765286187356836 + .005)) # Arredondar para cima
# print("{:<10}".format(234)) # Cria um campo com 10 caracteres a direita
# print("{:>10}".format(234)) # Cria um campo com 10 caracteres a esquerda
# print("{:05d}".format(234)) # Cria novos digítos
# print(" {0:d} {0:#x} {0:#d} {0:#b}".format(15)) # Vai imprimir "15 0xf 15 0b1111"

# cidade = 'Soterópolis'

# # Funções

# print(cidade.upper()) # Imprime tudo em maiúsculo
# print(cidade.lower()) # Imprime tudo em minúsculo
# print(cidade.title()) # Imprime a primeira letra em maiúsculo
# print("teste.teste".title())
# print("teste teste".title())
# print("      abc        ".strip()) # Remove os espaços em branco
# print("escrito abc trocou abc".replace("abc", "xyz")) # Troca

# # find e o index
# # Em outras linguagens é indexOf

# print("abcdef".find("d")) # Vai retornar a posição do caractere que está sendo localizado, somente a primeira ocorrência
# print("abcdf".find("h")) # Vai retornar -1, pois não está na string

# # Index traz o indice ou da erro

# print("abcdef".index("d")) # Vai retornar a posição do caractere que está sendo localizado, somente a primeira ocorrência
# print("abcdf".index("h")) # Quebra a aplicação e retorna o erro

# # #index traz o índice ou da erro
# # print("abcdefd".index("d"))
# # try:
# #     print("abcdefd".index("h"))
# # except:
# #     print("String not found!")

# if "abcde".find("h") == -1:
#   pass

# if "h" not in "abcde":
#   pass

# Atividades 

#Exercício 1:
#Solicite ao usuário que digite uma string e imprima o primeiro e o último caractere dessa string.

string = input("Digite qualquer coisa: ")

print(string[0])
print(string[-1])

#Exercício 2:
#Solicite ao usuário que digite uma string e imprima uma substring contendo os três primeiros caracteres.

print(string[0:3])

#Exercício 3:
#Solicite ao usuário que digite uma string e imprima uma substring contendo os três últimos caracteres.

inverso = string[::-1]
troca = inverso[0:3:]
teste = troca[::-1]
print(teste)

#Exercício 4:
#Solicite ao usuário que digite duas strings e as concatene, separando-as por um espaço.

#Exercício 5:
#Solicite ao usuário que digite uma string e converta todos os caracteres para maiúsculas.

#Solicite ao usuário que digite uma string e remova os espaços em branco do início e do fim.

#Solicite ao usuário que digite uma string e uma palavra a ser substituída, juntamente com a nova palavra. Imprima a string resultante após a substituição.

#Exercício 8:
#Solicite ao usuário que digite seu nome e idade, e formate uma mensagem usando f-strings.

#Solicite ao usuário que digite seu nome e idade, e formate uma mensagem usando a função format.

#Solicite ao usuário que digite um CEP e formate ##.###-### usando  usando a função format.

#Dada uma frase escrita pelo usuário, conte quantas plavras tem na frase:
#-Remova os espaços iniciais e finais
#-Remova os espaços contíguos

# Converta o nome para passagem área
# split()

"Murilo Freire Oliveira Araujo"
"ARAUJO, MURILO"
"Pedro Alvares Cabral"
"CABRAL, PEDRO"

nome = "Murilo Freire Oliveira Araujo"
print(list(nome)) # Lista com todos os caracteres
ultimo_nome = nome.split(" ")[-1].upper() # Vai tranformar em uma lista e depois pegar a última posição
primeiro_nome = nome.split(" ")[0].upper()
resultado = "{0}, {1}".format(ultimo_nome, primeiro_nome)
print(resultado)