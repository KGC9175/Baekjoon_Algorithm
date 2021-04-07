# 세탁소 사장 동혁
n = int(input())

for _ in range(n):
    m = int(input())
    q = m // 25
    d = (m % 25) // 10
    n = ((m % 25) % 10) // 5
    p = (((m % 25) % 10) % 5) // 1
    print(q, d, n, p)