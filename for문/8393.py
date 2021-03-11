# 1~n까지 합 구하기
n = int(input())
answer = 0

for i in range(1, n+1):
    answer += i

print(answer)