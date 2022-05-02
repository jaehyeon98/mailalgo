import sys

read = sys.stdin.readline

N, M, R = map(int, read().split())
index = min(N, M) >> 1
board = [list(map(int, read().split())) for _ in range(N)]
result = []

idx = 0
while idx < index:
    tmp = []
    for c in range(idx, M - idx):
        tmp.append(board[idx][c])
    for r in range(idx + 1, N - idx):
        tmp.append(board[r][M - idx - 1])
    for c in range(M - idx - 2, idx - 1, -1):
        tmp.append(board[N - idx - 1][c])
    for r in range(N - idx - 2, idx, -1):
        tmp.append(board[r][idx])
    length = len(tmp)
    i = R
    for c in range(idx, M - idx):
        board[idx][c] = tmp[i % length]
        i += 1
    for r in range(idx + 1, N - idx):
        board[r][M - idx - 1] = tmp[i % length]
        i += 1
    for c in range(M - idx - 2, idx - 1, -1):
        board[N - idx - 1][c] = tmp[i % length]
        i += 1
    for r in range(N - idx - 2, idx, -1):
        board[r][idx] = tmp[i % length]
        i += 1
    idx += 1

for r in range(N):
    result.append(' '.join(map(str, board[r])))
print('\n'.join(result))