# subprograma
def criaMatriz(lins, cols):
    matriz = []
    for lin in range(lins):
        matriz.append([0] * cols)
    return matriz


def preenche_matriz(min, max, matriz, lins, cols):
    from random import randint
    for lin in range(lins):
        for col in range(cols):
            matriz[lin][col] = randint(min, max)
    return matriz


def calcularMedia(matriz, lins, cols):
    rodada = 0
    for lin in range(lins):
        for col in range(cols):
            rodada += matriz[lin][col]
    media = rodada / (lins * cols)
    return media


def mediaAdquirida(mediaMin, media, lins, cols, min, max, matriz):
    teste = 1
    if media >= mediaMin:
        imp_matriz(lins, cols, matriz)
        mostrarImp(media, mediaMin, teste)
    else:
        while media < mediaMin:
            teste += 1
            if teste == 1000000:
                print("Após 1000000 de Tentativas, Nenhuma Média Superou o Limite Mínimo!!!")
                media = mediaMin
            else:
                matriz = preenche_matriz(min, max, matriz, lins, cols)
                media = calcularMedia(matriz, lins, cols)
        if teste != 1000000:
            imp_matriz(lins, cols, matriz)
            mostrarImp(media, mediaMin, teste)

    return None

def imp_matriz(lins, cols, matriz):
    print("Conteúdo da Matriz:")
    for i in range(lins):
        for j in range(cols):
            if (j == cols - 1):
                print("%d" % matriz[i][j], end=" ")
            else:
                print("%d" % matriz[i][j], end=" ")
        print()
    print()
def mostrarImp(media, media_min, testes):
    print(f"Limite da Média para Parar a Repetição: {media_min:0.2f}")
    print(f"Média dos Valores da Matriz: {media:0.2f}")
    print(f"Quantidade de tentativas para a média superar o limite mínimo: {testes}")
    return None
# principal
qtdLinhas, qtdColunas = map(int, input().split())
matrizZero = criaMatriz(qtdLinhas, qtdColunas)
valorMinimo, valorMaximo = map(int, input().split())
completarMatriz = preenche_matriz(valorMinimo, valorMaximo, matrizZero, qtdLinhas, qtdColunas)
mediaDaMatriz = calcularMedia(completarMatriz, qtdLinhas, qtdColunas)
media = float(input())
mediaAdquirida(media, mediaDaMatriz, qtdLinhas, qtdColunas, valorMinimo, valorMaximo, completarMatriz)
