def mostrar(prod, msg):
    print(msg)
    arquivo = open(prod, "r", encoding='UTF-8')
    for linha in arquivo:
        print("   ", linha, end="")
    arquivo.close()
    print()
    return None


def colocaProd(prod, prodAnterior):
    from os import remove, rename
    arquivo = open(prod, "r", encoding='UTF-8')
    arquivoTemporario = open(prod + "temp", "w", encoding='UTF-8')
    itemAdc = True
    for linha in arquivo:
        prodLinha = linha.split("#")
        codProd = prodLinha[0]
        novoprod = prodAnterior[0]
        if novoprod < codProd and itemAdc:
            arquivoTemporario.write(str("#".join(prodAnterior)) + "\n")
            arquivoTemporario.write(linha)
            itemAdc = False
        else:
            arquivoTemporario.write(linha)
    if itemAdc:
        arquivoTemporario.write(str("#".join(prodAnterior)))
    arquivo.close()
    arquivoTemporario.close()
    remove(prod)
    rename(prod + "temp", prod)
    return None


arq = input()
produto = input().split('#')
file = open(arq, 'r', encoding='UTF-8')
jaExiste = False
for codigo in file:
    ingredientes = codigo.split('#')
    if produto[0] == ingredientes[0]:
        print('Código já existe!!!')
        jaExiste = True
file.close()
if not jaExiste:
    mostrar(arq, "Conteúdo do %s antes:" % arq)
    print()
    colocaProd(arq, produto)
    mostrar(arq, "Conteúdo do %s depois:" % arq)
