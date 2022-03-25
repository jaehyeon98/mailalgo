# 꼼수부리지말고 정석대로 다 찾는방향부터 생각하자
# 망할 밑에 한줄만 검색하지 말고
import sys
from collections import deque
input = sys.stdin.readline
R = 12
C = 6
board = [list(input().rstrip()) for _ in range(12)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def eli_puyo(eli_list):
    for r, c in eli_list:
        board[r][c] = '.'

def fall():
    for c in range(C):
        for r in range(R - 2, -1, -1):
            for z in range(R - 1, r, -1):
                if board[r][c] != '.' and board[z][c] == '.':
                    board[z][c] = board[r][c]
                    board[r][c] = '.'
                    break



answer = 0
while True:
    visit = [[False] * C for _ in range(R)]
    flag = False
    target = []
    for i in range(R):
        for j in range(C):
            if board[i][j] == '.': continue
            if visit[i][j]: continue
            q = deque([(i, j)])
            visit[i][j] = True
            cnt = 1
            cand = set()
            cand.add((i, j))
            while q:
                r, c = q.popleft()
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if nr < 0 or nr >= R or nc < 0 or nc >= C: continue
                    if visit[nr][nc]: continue
                    if board[r][c] != board[nr][nc]: continue
                    visit[nr][nc] = True
                    cnt += 1
                    q.append((nr, nc))
                    cand.add((nr, nc))
            if cnt >= 4:
                flag = True
                target.extend(cand)
                eli_puyo(cand)
    if flag:
        answer += 1
        fall()
    else:
        break
print(answer)