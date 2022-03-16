from itertools import combinations

n, m = map(int, input().split())

check = [[False for _ in range(n+1)] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    check[a][b] = True
    check[b][a] = True

ice_cream = list(combinations(range(1, n + 1), 3))
ans = 0
for ice in ice_cream:
    if check[ice[0]][ice[1]] or check[ice[0]][ice[2]] or check[ice[1]][ice[2]]: # 하나라도 겹치는게 있으면
        continue
    ans += 1

print(ans)