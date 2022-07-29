# t = int(input())
# while t > 0:
#     t -= 1
#     n = int(input())
#     c = [int(x) for x in input().split()]
#     print(len(set(c)))


def pega_casos(carneiro):
    while carneiro > 0:
        carneiro -= 1
        qtd_carneiro = int(input())
        contando = [int(i) for i in input().split()]
        print(len(set(contando)))
    return None


casos = int(input())
pega_casos(casos)
