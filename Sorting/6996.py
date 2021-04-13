# 애너그램
n = int(input())

for _ in range(n):
    lst = list(map(str, input().split(' ')))
    
    lst_1st = list(lst[0])
    lst_2nd = list(lst[1])
    lst_1st.sort()
    lst_2nd.sort()
    
    if lst_1st == lst_2nd:
        print(lst[0], '&', lst[1], 'are anagrams.')
    else:
        print(lst[0], '&', lst[1], 'are NOT anagrams.')