# 숫자의 합
N = int(input())
lst = list(map(int, input()))
answer = 0

for i in lst:
    answer += i

print(answer)