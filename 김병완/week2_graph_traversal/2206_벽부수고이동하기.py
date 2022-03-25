# NOT YET
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().rstrip())) for _ in range(N)]
if N == 1 and M == 1:
    print(1)
    exit()

visit = [[-1] * M for _ in range(N)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

q = deque([(0, 0, 1, True)])
visit[0][0] = 1
# answer = -1
while q:
    flag = False
    r, c, cnt, cheat = q.popleft()
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if nr < 0 or nr >= N or nc < 0 or nc >= M: continue
        if visit[nr][nc] != -1 and visit[nr][nc] < cnt + 1: continue
        if board[nr][nc] == 1:
            if not cheat: continue
            visit[nr][nc] = cnt + 1
            q.append((nr, nc, cnt + 1, False))
            continue
        if nr == N - 1 and nc == M - 1:
            # answer = cnt + 1
            visit[nr][nc] = cnt + 1
            flag = True
            break
        visit[nr][nc] = cnt + 1
        q.append((nr, nc, cnt + 1, cheat))
    if flag:
        break

print(visit[N - 1][M - 1])