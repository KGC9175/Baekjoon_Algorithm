# 평균은 넘겠지
c = int(input())

for i in range(c):
    sum = 0
    lst = list(map(int, input().split()))

    for j in lst:
        sum += j
    
    n = lst[0]
    count = 0
    sum -= n
    avg = sum / n
    lst.reverse()

    for k in lst[0:n]:
        if avg < k:
            count += 1
    
    answer = count / n * 100

    print(str('%0.3f' % float(answer)) + '%')