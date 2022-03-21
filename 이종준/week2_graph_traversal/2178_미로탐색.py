from collections import deque

N, M = map(int, input().split())
data = [[0] * M for _ in range(N)]
q = deque()
# 우하좌상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs():
    while q:
        r, c, cnt = q.popleft()
        if r == N - 1 and c == M - 1:
            print(cnt)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and data[nr][nc] == 1:
                q.append((nr, nc, cnt + 1))
                visited[nr][nc] = 1


for i in range(N):
    arr = input()
    for j in range(M):
        data[i][j] = int(arr[j])
visited = [[0] * M for _ in range(N)]
q.append((0, 0, 1))
visited[0][0] = 1

bfs()