# 쉽게 푸는 문제
A, B = map(int, input().split())
lst1 = []
answer = 0

for i in range(B+1):
    i = [i] * i
    lst1 = lst1 + i

for j in lst1[A-1:B]:
    answer += j

print(answer)