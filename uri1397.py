while True:
    casos = int(input())
    if casos == 0:
        break
    a, b = [0, 0]
    for i in range(casos):
        num, num2 = list(map(int, input().split()))
        if num > num2:
            a += 1
        elif num < num2:
            b += 1
    print(f'{a} {b}')
