# 제곱근

n = int(input())
low, high = 1, n

while True:
    mid = (low + high) // 2
    if mid ** 2 == n:
        print(mid)
        break
    elif mid ** 2 > n:
        high = mid - 1
    elif mid ** 2 < n:
        low = mid + 1