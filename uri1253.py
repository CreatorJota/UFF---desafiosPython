ALFABETO = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
casos = int(input())
for _ in range(casos):
    string = ''
    palavra = input()
    desloca = int(input())
    for i in range(len(palavra)):
        letra = palavra[i]
        indexLetra = ALFABETO.index(letra)
        trocaDeIndex = indexLetra - desloca
        decripto = ALFABETO[trocaDeIndex]
        string += decripto
    print(string)
    