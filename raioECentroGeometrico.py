def pegaValores(vals):
    listaCoord = []
    listaCoord.append((int(vals[0]), int(vals[1])))
    while vals != []:
        vals = input().split()
        if vals != []:
            listaCoord.append((int(vals[0]), int(vals[1])))
    return listaCoord


def calcular(vals):
    somaValoresUm = 0
    somarValoresDois = 0
    comprimento = len(vals)
    for i in range(comprimento):
        somaValoresUm += vals[i][0]
        somarValoresDois += vals[i][1]
    valorUm = somaValoresUm / comprimento
    valorDois = somarValoresDois / comprimento
    return valorUm, valorDois


def achandoRaio(vals, valorUm, valorDois):
    tamanho = len(vals)
    raio = ((vals[0][0] - valorUm) ** 2 + (vals[0][1] - valorDois) ** 2) ** (1 / 2)
    for i in range(tamanho):
        alternativo = ((vals[i][0] - valorUm) ** 2 + (vals[i][1] - valorDois) ** 2) ** (1 / 2)
        if alternativo > raio:
            raio = alternativo
    return raio


valores = input().split()
if valores != []:
    listaDosValores = pegaValores(valores)
    valorUm, valorDois = calcular(listaDosValores)
    maiorRaio = achandoRaio(listaDosValores, valorUm, valorDois)
    print(f"Centro Geométrico: (%0.2f, %0.2f) e Raio: %0.2f" % (valorUm, valorDois, maiorRaio))
else:
    print("Nenhum Ponto Foi Lido!!!")
