#
from collections import deque


def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    visit[si][sj] = True
    tmp.append((si, sj))
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < 12 and 0 <= nj < 6:
                if not visit[ni][nj] and puyo[ni][nj] == puyo[i][j]:
                    visit[ni][nj] = True
                    q.append((ni, nj))
                    tmp.append((ni, nj))


def fall():
    for j in range(6):
        for i in range(10, -1, -1):
            for z in range(11, i, -1): # j로 썼었음...... 미친거임...
                if puyo[i][j] != '.' and puyo[z][j] == '.':
                    puyo[z][j] = puyo[i][j]
                    puyo[i][j] = '.'
                    break


puyo = [list(input()) for _ in range(12)]
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
ans = 0

while True:
    visit = [[False] * 6 for _ in range(12)]
    flag = 0
    for si in range(12):
        for sj in range(6):
            if puyo[si][sj] != '.' and not visit[si][sj]:
                tmp = []
                bfs(si, sj)
                if len(tmp) >= 4:
                    flag = 1
                    for a, b in tmp:
                        puyo[a][b] = '.'

    if flag == 0:
        break
    else:
        ans += 1
        fall()

print(ans)
