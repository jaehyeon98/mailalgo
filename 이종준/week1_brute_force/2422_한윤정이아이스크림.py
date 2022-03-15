# 진행중
from itertools import combinations

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(M)]

arr = [[0] * (N + 1) for _ in range(N + 1)]
for i in data:
    r, c = i[0], i[1]
    arr[r] = c
    arr[c] = r


num_list = [i for i in range(1, N + 1)]
for comb in list(combinations(num_list, M)):
    print(comb)