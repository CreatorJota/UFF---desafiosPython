[hastes, altura] = list(map(int, input().split()))
h = list(map(int, input().split()))
for i in h:
    valor = 0
    valorDois = 0
    if h[i] > altura:
        while h[i] != altura:
            valor += h[0] - 1
            valorDois += h[1] - 1
            print(valor, valorDois)
