#최댓값 순서 찾기
lst = []

for i in range(9):
    lst.append(int(input()))

lst_copy = lst.copy()
lst_copy.sort()

n = lst_copy[8]
m = lst.index(n) + 1

print(n)
print(m)