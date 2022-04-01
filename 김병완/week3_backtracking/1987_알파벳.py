import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]

alpha = set()
alpha.add(board[0][0])
answer = 0
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dfs(s, r, c):
    global answer
    answer = max(answer, s)
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if nr < 0 or nr >= R or nc < 0 or nc >= C or board[nr][nc] in alpha: continue
        # if board[nr][nc] in alpha:
        #     continue
        alpha.add(board[nr][nc])
        dfs(s + 1, nr, nc)
        alpha.remove(board[nr][nc])

dfs(1, 0, 0)
print(answer)
