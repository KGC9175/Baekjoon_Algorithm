# 더하기 싸이클
n = int(input())
m = n
answer = 0

while True:
    a = n % 10
    b = (n // 10) + (n % 10)
    c = b % 10
    n = (a * 10) + (b % 10)
    answer += 1
    if n == m:
        break

print(answer)