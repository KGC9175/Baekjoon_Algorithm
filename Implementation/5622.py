# 다이얼
x = list(str(input()))
lst = []
answer = 0

for i in x:
    if i == 'A' or i == 'B' or i == 'C':
        lst.append(2)

    elif i == 'D' or i == 'E' or i == 'F':
        lst.append(3)
    
    elif i == 'G' or i == 'H' or i == 'I':
        lst.append(4)

    elif i == 'J' or i == 'K' or i == 'L':
        lst.append(5)

    elif i == 'M' or i == 'N' or i == 'O':
        lst.append(6)

    elif i == 'P' or i == 'Q' or i == 'R' or i == 'S':
        lst.append(7)

    elif i == 'T' or i == 'U' or i == 'V':
        lst.append(8)
    
    elif i == 'W' or i == 'X' or i == 'Y' or i == 'Z':
        lst.append(9)

for i in lst:
    answer = answer + i + 1

print(answer)