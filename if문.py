# 1330번
A, B = map(int, input().split())

if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')

# 9498번
n = int(input())

if n >= 90:
    print('A')
elif n >= 80:
    print('B')
elif n >= 70:
    print('C')
elif n >= 60:
    print('D')
else:
    print('F')

# 2753번(윤년)
n = int(input())

if (n % 4 == 0) and ((n % 100 != 0) or (n % 400 == 0)):
    print('1')
else:
    print('0')

# 14681번(사분면 고르기)
x = int(input())
y = int(input())

if x > 0 and y > 0:
    print('1')
elif x < 0 and y > 0:
    print('2')
elif x < 0 and y < 0:
    print('3')
elif x > 0 and y < 0:
    print('4')

# 2884번(알람시계)
h, m = map(int, input().split())

if m >= 45:
    print(h, m - 45)
else:
    if h == 0:
        print(23, m + 15)
    else:
        print(h - 1, m + 15)