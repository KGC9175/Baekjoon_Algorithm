# 로프
n = int(input())
lst = []

for _ in range(n):
    rope = int(input())
    lst.append(rope)

lst.sort()
lst.reverse()

for i in range(n):
    lst[i] = lst[i] * (1 + i)

print(max(lst))