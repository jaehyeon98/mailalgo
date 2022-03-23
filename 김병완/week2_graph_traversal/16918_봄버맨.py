import sys
from collections import deque
input = sys.stdin.readline

def convert(li):
    tmp = []
    for i in range(R):
        tmp.append(''.join(li[i]))
    return '\n'.join(tmp)

R, C, N = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N -= 1
while N:
    q = deque()
    for r in range(R):
        for c in range(C):
            if board[r][c] == 'O':
                q.append((r, c))
            else:
                board[r][c] = 'O'
    N -= 1
    if N == 0:
        break
    while q:
        r, c = q.popleft()
        board[r][c] = '.'
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if nr < 0 or nr >= R or nc < 0 or nc >= C: continue
            board[nr][nc] = '.'
    N -= 1

print(convert(board))
    




