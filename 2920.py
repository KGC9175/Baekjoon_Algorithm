# 음계
a, b, c, d, e, f, g, h = map(int, input().split())

if [a, b, c, d, e, f, g, h] == [1, 2, 3, 4, 5, 6, 7, 8]:
    print('ascending')
elif [a, b, c, d, e, f, g, h] == [8, 7, 6, 5, 4, 3, 2, 1]:
    print('descending')
else:
    print('mixed')