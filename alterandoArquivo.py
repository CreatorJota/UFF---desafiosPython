def invert(word):
    return word[::-1]


def printando(nomeArq, msg):
    print(msg)
    arquivo = open(nomeArq, "r")
    for dado in arquivo:
        print("   ", dado, end="")
    arquivo.close()
    return None


def mudandoPalavra(arquivo, escolhido, inv):
    from os import remove, rename
    file = open(arquivo, 'r')
    fileTemp = open(arquivo + 'subs', 'w')
    for linha in file:
        fileTemp.write(invertendo(linha, escolhido, inv) + "\n")
    file.close()
    fileTemp.close()
    remove(arquivo)
    rename(arquivo + "subs", arquivo)
    return None


def invertendo(linha, escolhido, invertido):
    frase = linha.split()
    if escolhido in frase:
        indice = frase.index(escolhido)
        frase.insert(indice, invertido)
        frase.remove(escolhido)
    return ' '.join(frase)


arq = input()
NomeEscolhido = input()
inverte = invert(NomeEscolhido)
printando(arq, "Arquivo %s antes das inversões de %s:" % (arq, NomeEscolhido))
print()
mudandoPalavra(arq, NomeEscolhido, inverte)
printando(arq, "Arquivo %s depois das inversões de %s:" % (arq, NomeEscolhido))
