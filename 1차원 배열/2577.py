#숫자의 개수
x = int(input())
y = int(input())
z = int(input())
n = x * y * z
lst = []

for i in str(n):
    lst.append(i)

for i in range(0,10):
    print(lst.count(str(i)))