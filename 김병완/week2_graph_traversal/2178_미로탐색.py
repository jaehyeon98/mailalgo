import sys
from collections import deque
sys.stdin = open('2178.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
board = [input().rstrip() for _ in range(N)]

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
visit = [[-1] * M for _ in range(N)]

q = deque()
q.append((0, 0, 1))
visit[0][0] = 1

while q:
    r, c, depth = q.popleft()
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if nr < 0 or nr >= N or nc < 0 or nc >= M: continue
        if board[nr][nc] == '0': continue
        if visit[nr][nc] != -1: continue
        visit[nr][nc] = depth + 1
        q.append((nr, nc, depth + 1))

print(visit[N - 1][M - 1])

