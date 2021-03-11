# 캠핑
L, P, V = 1, 1, 1
n = 0

while L > 0 and P > 0 and V > 0:
    L, P, V = map(int, input().split())
    if L > 0 and P > 0 and V > 0: 
        n += 1
        print((V // P) * L, (V % P), n)
    else:
        break