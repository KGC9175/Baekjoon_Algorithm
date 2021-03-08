# 거스름돈
n = int(input())
m = 1000 - n
count = 0

change_array = [500, 100, 50, 10, 5, 1]

for coin in change_array:
    count = count + m // coin
    m = m % coin

print(count)