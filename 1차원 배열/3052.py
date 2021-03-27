#나머지 구분
lst= []
count = 0

for i in range(10):
    lst.append(int(input()))

for i in range(0, 10):
    lst[i] = lst[i] % 42

for i in range(42):
    if i in lst:
        count += 1

print(count)