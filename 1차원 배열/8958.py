# OX퀴즈
n = int(input())

for i in range(n):
    m = input()
    lst = list(m)
    score = 1
    sum = 0

    for j in lst:
        if j == 'O':
            sum += score
            score += 1
        else:
            score = 1

    print(sum)