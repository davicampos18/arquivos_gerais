def analise_vendas(vendas:list):
    # TODO: Calcule o total de vendas e realize a média mensal:
    total_vendas = 0
    for numero in vendas:
        total_vendas = total_vendas + numero
    media_vendas = total_vendas / len(vendas)

    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    numeros = []
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    dados_separados = entrada.split(',')
    for numero in dados_separados:
        num = numero.strip()
        numeros.append(num)
    # TODO: Converta a entrada em uma lista de inteiros:
    dados_inteiros = map(int, numeros)
    vendas = list(dados_inteiros)
    return vendas

vendas = obter_entrada_vendas()
print(analise_vendas(vendas))