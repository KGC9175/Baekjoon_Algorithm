# Presents
n = int(input())
lst = []

for i in range(n):
    lst.append(float(input()))

lst.sort()

print('%.2f' %lst[1])