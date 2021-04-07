# 프로그래밍 경시대회
n = int(input())
lst = []

for i in range(n):
    lst.append(list(map(int, input().split())))

print(lst, list(lst[0]))

