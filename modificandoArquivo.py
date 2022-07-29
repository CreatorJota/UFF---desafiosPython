from os import remove, rename


def mostra(arq, msg):
    print(msg)
    arquivo = open(arq, 'r', encoding='utf-8')
    for j in arquivo:
        print(j, end="")
    arquivo.close()
    return None


def mudando(linhas, palavraSai):
    palavra = linhas.split()
    for i in palavra:
        if i not in palavraSai:
            temporario.write(i + " ")
    return None


palavraDesejada = input()
saiPalavra = set()
saiPalavra.add(palavraDesejada)
while palavraDesejada != '':
    saiPalavra.add(palavraDesejada)
    palavraDesejada = input()
print(saiPalavra)
dados = input()
file = open(dados, "r", encoding="utf-8")
temporario = open(dados + "novo", "w", encoding="utf-8")
mostra(dados, 'Arquivo %s antes de ser alterado:' % dados)
for linha in file:
    mudando(linha, saiPalavra)
    temporario.write("\n")
temporario.close()
file.close()
remove(dados)
rename(dados + "novo", dados)
print()
mostra(dados, 'Arquivo %s depois de ser alterado:' % dados)
