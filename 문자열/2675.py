# 문자열 반복
T = int(input())

for _ in range(T):
    N = list(input().split())
    m = list(N[1])
    for i in m:
        print(i * int(N[0]), end='')
    print()