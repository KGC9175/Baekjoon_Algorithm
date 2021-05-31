# 소수의 연속합
import sys
input = sys.stdin.readline

n = int(input())
array = [True for i in range(n + 1)]
lst = []
answer, end = 0, 0
interval_sum = 0

for j in range(2, int(n ** 0.5) + 1):
    if array[j] == True:
        k = 2
        while j * k <= n:
            array[j * k] = False
            k += 1

for l in range(2, n + 1):
    if array[l]:
        lst.append(l)

for start in range(len(lst)):
    while interval_sum < n and end < len(lst):
        interval_sum += lst[end]
        end += 1
    if interval_sum == n:
        answer += 1
    interval_sum -= lst[start]

print(answer)