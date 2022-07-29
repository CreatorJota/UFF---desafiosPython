def num_rodadas(casos):
    rodadas = int(input())
    if rodadas != 0:
        casos += 1
        par_impar(rodadas, casos)


def par_impar(rodadas, casos):
    nome_par = input()
    nome_impar = input()
    print('Teste', casos)
    jogadores = []
    for rodada in range(rodadas):
        a, b = map(int, input().split())
        if (a + b) % 2 == 0:
            jogadores.append(nome_par)
        else:
            jogadores.append(nome_impar)
    for jogador in jogadores:
        print(jogador)
    print()
    num_rodadas(casos)


if __name__ == '__main__':
    teste = 0
    num_rodadas(teste)
