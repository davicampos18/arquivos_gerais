def produto_mais_vendido(produtos):
    contagem = {}
    
    for produto in produtos:
        if produto in contagem:
            contagem[produto] += 1
        else:
            contagem[produto] = 1
    
    max_produto = None
    max_count = 0
    valores = []
    
    for produto, count in contagem.items():
        valores.append(count)
    
    max_count = max(valores)
    for produto, count in contagem.items():
        if count == max_count:
            max_produto = produto


    return max_produto

def obter_entrada_produtos():
    # Solicita a entrada do usuário em uma única linha
    produtos = []
    entrada = input()
    # TODO: Converta a entrada em uma lista de strings, removendo espaços extras:
    dados_separados = entrada.split(",")
    for produto in dados_separados:
        inserir = produto.strip()
        produtos.append(inserir)

    
    return produtos


produtos = obter_entrada_produtos()
print(produto_mais_vendido(produtos))