# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
M = int(input())

parent = [0] * (N + 1)
for i in range(1, N + 1):
    parent[i] = i

for _ in range(M):
    x, y = map(int, input().split())
    for i in range(x + 1, y + 1):
        union_parent(parent, x, i)

for i in range(1, N + 1):
    find_parent(parent, i)

parent = set(parent)
print(len(list(parent)) - 1)