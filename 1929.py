# 소수 구하기
m, n = map(int, input().split())

array = [True for i in range(n + 1)]

for i in range(2, int(n ** 0.5) + 1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[(i * j)] = False
            j += 1

array[1] = False

for k in range(m, n + 1):
    if array[k]:
        print(k)