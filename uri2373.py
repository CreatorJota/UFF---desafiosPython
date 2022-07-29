casos = int(input())
acum = 0
for i in range(casos):
    bandeja = list(map(int, input().split()))
    for j in bandeja:
        if j > bandeja[1]:
            acum += bandeja[1]
print(acum)
