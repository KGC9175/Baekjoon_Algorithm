# 컵홀더

N = int(input())
array = list(str(input()))
x = array.count('L')

print(min(int((N - (x / 2)) + 1), N))