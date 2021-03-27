#최소, 최대
N = int(input())
lst = list(map(int, input().split()))
lst.sort()

print(lst[0], lst[N-1])