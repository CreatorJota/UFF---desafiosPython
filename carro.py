[aX0, aY0, aX1, aY1] = list(map(int, input().split()))
[bX0, bY0, bX1, bY1] = list(map(int, input().split()))

if aX0 <= bX0 <= aX1 or aX0 <= bX1 <= aX1 or bX0 <= aX0 <= bX1 or bX0 <= aX1 <= bX1:
    if aY0 <= bY0 <= aY1 or aY0 <= bY1 <= aY1 or bY0 <= aY0 <= bY1 or bY0 <= aY1 <= bY1:
        print(1)
    else:
        print(0)
else:
    print(0)
