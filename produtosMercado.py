def recebeProdutos(qtdProd):
    produtoGeral = []
    for i in range(qtdProd):
        produto = input().split("#")
        produto[2] = int(produto[2])
        produto[3] = float(produto[3])
        produtoGeral.append(tuple(produto))
    return produtoGeral


def localizaBarato(produto, qtdProd):
    maisBarato = produto[0][3]
    localizarBarato = 0
    for i in range(qtdProd):
        if maisBarato > produto[i][3]:
            maisBarato = produto[i][3]
            localizarBarato = i
    print(f"Produto Mais Barato: {produto[localizarBarato]}")
    return None


def localizaCaro(produto, qtdProd):
    maisCaro = produto[0][3]
    localizacaoDoCaro = 0
    for i in range(qtdProd):
        if maisCaro < produto[i][3]:
            maisCaro = produto[i][3]
            localizacaoDoCaro = i
    print(f"Produto Mais Caro: {produto[localizacaoDoCaro]}")
    return None


def monteDeUnid(produto, qtdPrd):
    acumulador = 0
    for i in range(qtdPrd):
        acumulador += produto[i][2]
    print(f"Quantidade de Unidades no Mercado: {acumulador}")
    return None


def total(produto, qtdPrd):
    acumulador = 0
    for i in range(qtdPrd):
        acumulador += produto[i][2] * produto[i][3]
    print(f"Valor Total do Estoque: R$ {acumulador:0.2f}")
    return None


quantidadePrd = int(input())
if quantidadePrd != 0:
    listaPrd = recebeProdutos(quantidadePrd)
    localizaBarato(listaPrd, quantidadePrd)
    localizaCaro(listaPrd, quantidadePrd)
    monteDeUnid(listaPrd, quantidadePrd)
    total(listaPrd, quantidadePrd)
else:
    print("Nenhum Produto Foi Lido!!!")
