def pegaValores(num):
    while num > 0:
        num -= 1
        cod = input().split()
        cod.sort(key=len, reverse=True)
        for i in range(len(cod)):
            print(cod[i], end='')
            if i != len(cod) - 1:
                print(' ', end='')
        print()
    return None


n = int(input())
pegaValores(n)
