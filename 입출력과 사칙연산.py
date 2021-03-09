# 1000번
A, B = map(int, input().split())

print(A + B)

# 1001번
A, B = map(int, input().split())

print(A - B)

# 10998번
A, B = map(int, input().split())

print(A * B)

# 1008번
A, B = map(int, input().split())

print(A / B)

# 10869번
A, B = map(int, input().split())
print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)

# 10430번
A, B, C = map(int, input().split())
print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)

# 2588번
n = int(input())
m = list(map(int, input()))

print(n * m[2])
print(n * m[1])
print(n * m[0])

print(n * (m[0]*100 + m[1]*10 + m[2]))