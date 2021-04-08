# 열 개씩 끊어 출력하기
c = list(str(input()))

while True:
    if len(c) > 9:
        for i in range(10):
            print(c[i], end='')
        print('')
        del c[0:10]
    else:
        for i in range(len(c)):
            print(c[i], end='')
        break