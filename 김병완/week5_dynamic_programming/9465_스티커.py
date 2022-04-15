import sys
read = sys.stdin.readline

for tc in range(int(read())):
    n = int(read())
    board = [list(map(int, read().split())) for _ in range(2)]
    if n == 1:
        print(max(board[0][0], board[1][0]))
        continue
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = board[0][0]
    dp[1][0] = board[1][0]
    dp[0][1] = board[0][1] + board[1][0]
    dp[1][1] = board[1][1] + board[0][0]
    for i in range(2, n):
        dp[0][i] = board[0][i] + max(dp[0][i - 2], dp[1][i - 1], dp[1][i - 2])
        dp[1][i] = board[1][i] + max(dp[1][i - 2], dp[0][i - 1], dp[0][i - 2])

    print(max(dp[0][n - 1], dp[1][n - 1]))
