participantes = int(input())
sequencia = input().split()
qtd = []
for i in sequencia:
    ind = sequencia.index(i)
    if i == ind:
        qtd.append(i)
print(qtd)
