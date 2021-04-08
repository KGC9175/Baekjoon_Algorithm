# 상수
x = list(map(str, input().split()))
n = list(x[0])
m = list(x[1])
n.reverse()
m.reverse()

if int(n[0] + n[1] + n[2]) > int(m[0] + m[1] + m[2]):
    print(int(n[0] + n[1] + n[2]))
else:
    print(int(m[0] + m[1] + m[2]))