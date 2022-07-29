n = int(input())
palavras = [input() for _ in range(n)]
for palavra in palavras:
    criptoUm = "".join(
        chr(ord(letra) + 3) if letra.isalpha() else letra for letra in palavra
    )
    criptoDois = criptoUm[::-1]
    metade = int(len(criptoDois) / 2)
    metadeUm = criptoDois[:metade]
    metadeDois = criptoDois[metade:]
    criptoTres = metadeUm + ''.join(
        chr(ord(letra) - 1) for letra in metadeDois
    )
    print(criptoTres)
