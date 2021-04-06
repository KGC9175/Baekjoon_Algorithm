# 콘테스트
w_lst = []
k_lst = []

for i in range(10):
    w_lst.append(int(input()))

for i in range(10):
    k_lst.append(int(input()))

w_lst.sort(reverse=True)
k_lst.sort(reverse=True)

print(w_lst[0]+w_lst[1]+w_lst[2], k_lst[0]+k_lst[1]+k_lst[2])