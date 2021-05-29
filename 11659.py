# 구간 합 구하기 4
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

sum_value = 0
prefix_sum = [0]
for k in data:
    sum_value += k
    prefix_sum.append(sum_value)

for _ in range(m):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i - 1])