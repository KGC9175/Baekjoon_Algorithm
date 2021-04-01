# 알파벳 찾기
S = list(map(str, input()))
lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in lst:
    try:
        print(S.index(i), end=' ')
    except ValueError:
        print(-1, end=' ')