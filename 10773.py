# 제로
k = int(input())
lst = []

for i in range(0, k):
    n = int(input())
    if n > 0:
        lst.append(n)
    else:
        if len(lst) == 0:
            continue
        lst.pop()

print(sum(lst))