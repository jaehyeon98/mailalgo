import sys

read = sys.stdin.readline

board = [list(map(int, read().split())) for _ in range(19)]
visit = [[False] * 19 for _ in range(19)]

def isVictory(r, c, who):
    d = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    for i in range(8):
        cnt = 0
        nr = r
        nc = c
        while 0 <= nr < 19 and 0 <= nc < 19 and board[nr][nc] == who:
            cnt += 1
            nr += d[i][0]
            nc += d[i][1]

        if cnt == 5 and board[r - d[i][0]][c - d[i][1]] != who:
            return True
    return False

winner = 0
idx_r = 0
idx_c = 0
for c in range(19):
    flag = False
    for r in range(19):
        if board[r][c] != 0:
            if isVictory(r, c, board[r][c]):
                winner = board[r][c]
                idx_r = r + 1
                idx_c = c + 1
                flag = True
                break
    if flag:
        break

if winner == 0:
    print(winner)
else:
    print(winner)
    print(idx_r, idx_c)
