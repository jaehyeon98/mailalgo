import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def melt(r, c):
    for i in range(4):
        nr = dr[i] + r
        nc = dc[i] + c
        if 0 <= nr < N and 0 <= nc < M and data[nr][nc] == 0 and not visited[nr][nc]:
            data[r][c] = data[r][c] - 1
            if data[r][c] <= 0:
                data[r][c] = 0

def bfs():
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and not bfs_visited[nr][nc] and data[nr][nc]:
                bfs_visited[nr][nc] = 1
                q.append((nr, nc))
    return 1

q = deque()
ans = 0

while True:
    flag = False
    visited = [[0] * M for _ in range(N)]
    ans += 1
    for i in range(N):
        for j in range(M):
            if data[i][j] and not visited[i][j]:
                flag = True
                visited[i][j] = 1
                melt(i, j)

    if flag == False:
        ans = 0
        break
    
    tmp = 0
    bfs_visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if data[i][j] and not bfs_visited[i][j]:
                q.append((i, j))
                bfs_visited[i][j] = 1
                tmp += bfs()

    if tmp >= 2:
        break
    
print(ans)