n = int(input())
for i in range(n):
    alunos = int(input())
    nota = list(map(int, input().split()))
    notaTrocada = sorted(nota, reverse=True)
    nao_mudou = alunos
    for j in range(alunos):
        if notaTrocada[j] != nota[j]:
            nao_mudou -= 1
    print(nao_mudou)
