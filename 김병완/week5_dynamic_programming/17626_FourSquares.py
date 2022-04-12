import sys
read = sys.stdin.readline

N = int(read())
dp = [0] * (N + 1)
for i in range(1, N + 1):
    if i ** 2 > N: break
    dp[i] = i ** 2



