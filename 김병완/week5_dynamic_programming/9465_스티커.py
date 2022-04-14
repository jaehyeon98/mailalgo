import sys
read = sys.stdin.readline

for tc in range(int(read())):
    n = int(read())
    board = [list(map(int, read().split())) for _ in range(2)]
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = board[0][0]
    dp[1][0] = board[1][0]
    for i in range(1, n):
        dp[i][0] = max()
