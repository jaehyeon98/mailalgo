import sys
read = sys.stdin.readline

N = int(read())
board = [list(map(int, read().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for r in range(N):
    for c in range(N):
        if r == N - 1 and c == N - 1:
            print(dp[r][c])
            break
        nr = r + board[r][c]
        nc = c + board[r][c]
        if nr < N:
            dp[nr][c] += dp[r][c]
        if nc < N:
            dp[r][nc] += dp[r][c]
