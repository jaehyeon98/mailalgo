import sys
read = sys.stdin.readline

board = []
n = int(read())
for i in range(n):
    board.append(int(read()))

dp = [0] * n
dp[0] = board[0]
dp[1] = board[0] + board[1]
dp[2] = max(dp[1] + board[2], dp[0] + board[2])

for k in range(3, n):
    dp[k] = max(board[k] + dp[k - 1] + dp[k - 3], board[k] + dp[k - 2])

print(dp[n - 1])
