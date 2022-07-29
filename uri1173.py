def ler(valores):
    valores[0] = int(input())
    print(f'N[0] = {valores[0]}')
    for i in range(1, len(valores)):
        valores[i] = valores[i - 1] * 2
        print(f'N[{i}] = {valores[i]}')
    return None


lista = [0.0] * 10
ler(lista)
