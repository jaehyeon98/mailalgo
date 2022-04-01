# 못 풀었음 ㅜㅜ

from collections import deque

data = [list(input()) for _ in range(5)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

visited = [[0] * 5 for _ in range(5)]
my_set = set()

def dfs(r, c, cnt, my_str):
    global my_set
    global ans
    visited[r][c] = 1
    if cnt == 7:
        if my_str in my_set:
            return
        tmp = 0
        for j in range(7):
            if my_str[j] == 'S':
                tmp += 1
        if tmp >= 4:
            ans += 1
            my_set.add(my_str)
        return
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < 5 and 0 <= nc < 5 and not visited[nr][nc]:
            dfs(nr, nc, cnt + 1, my_str + data[nr][nc])
            visited[nr][nc] = 0

ans = 0

for i in range(5):
    for j in range(5):
        visited = [[0] * 5 for _ in range(5)]
        dfs(i, j, 1, data[i][j])

print(ans)