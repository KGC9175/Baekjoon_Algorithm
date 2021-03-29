#평균조작
N = int(input())
lst = list(map(int, input().split()))
lst_copy = lst.copy()
lst.sort()
M = lst[N-1]
sum = 0

for i in lst_copy:
    lst.append(i / M * 100)

lst.reverse()

for i in range(1, N+1):
    sum += lst[i-1]

print(sum / N)