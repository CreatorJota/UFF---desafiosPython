import math


def recebe(vals):
    listadosVals = []
    for i in vals:
        listadosVals.append(int(i))
    largura = listadosVals[0]
    altura = listadosVals[1]
    profundidade = listadosVals[2]
    raio = listadosVals[3]
    volume = largura*profundidade*altura
    volumeEsfera = (4*math.pi*(raio**3))/3
    if volume < volumeEsfera:
        print("S")
    else:
        print("N")
    return None


valores = input().split()
if valores != 0:
    recebe(valores)
