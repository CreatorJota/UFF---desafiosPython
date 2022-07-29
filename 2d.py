casos = int(input())
REGRA = {'ESQ': -1, 'DIR': 1}
for i in range(casos):
    comandos = int(input())
    eixoX = 0
    pegaValor = [0]
    for j in range(1, comandos + 1):
        mandei = input()
        if 'EXEC' not in mandei:
            pegaValor.append(REGRA[mandei])
            eixoX += REGRA[mandei]
        else:
            EXEC = int(mandei[-1])
            valorDoExec = pegaValor[EXEC]
            pegaValor.append(valorDoExec)
            eixoX += valorDoExec
    print(eixoX)
