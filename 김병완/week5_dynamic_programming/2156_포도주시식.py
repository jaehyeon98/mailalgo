import sys
read = sys.stdin.readline

board = []
n = int(read())
for i in range(n):
    board.append(int(read()))


dp = [0] * n
if n == 1:
    print(board[0])
    exit()
elif n == 2:
    print(board[0] + board[1])
    exit()

dp[0] = board[0]
dp[1] = board[0] + board[1]
dp[2] = max(board[2] + board[1], board[2] + board[0], dp[1])

for k in range(3, n):
    dp[k] = max(board[k] + board[k - 1] + dp[k - 3], board[k] + dp[k - 2], dp[k - 1])

print(dp[n - 1])
