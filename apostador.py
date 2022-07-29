def mostra(dic):
    for i in range(6, 2, -1):
        print(f"CPF'S que tiveram {i} acertos:")
        if dic.get(i) == set():
            print(f'Nenhum acerto para {i} números')
        else:
            for j in dic[i]:
                print(j)
        print()
    return None


def resolve(arquivo, num):
    tresA = set()
    quatroA = set()
    cincoA = set()
    seisA = set()
    dic = dict()
    dados = open(arquivo, "r", encoding="utf-8")
    for linha in dados:
        conta = 0
        cpf, num1, num2, num3, num4, num5, num6 = linha.strip("\n").split('#')
        for i in num:
            if str(i) in [num1, num2, num3, num4, num5, num6]:
                conta += 1
        if conta == 6:
            seisA.add(int(cpf))
        elif conta == 5:
            cincoA.add(int(cpf))
        elif conta == 4:
            quatroA.add(int(cpf))
        elif conta == 3:
            tresA.add(int(cpf))
    dic[6] = seisA
    dic[5] = cincoA
    dic[4] = quatroA
    dic[3] = tresA
    mostra(dic)
    dados.close()
    return None


Arq = input()
numSorteado = list(map(int, input('Números sorteados: ').split()))
resolve(Arq, numSorteado)
