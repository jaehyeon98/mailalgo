import sys

read = sys.stdin.readline

for t in range(int(read())):
    N = int(read())
    if N <= 3:
        print(1)
        continue
    dp = [1, 1, 1]
    for i in range(3, N):
        dp.append(dp[i - 2] + dp[i - 3])
    print(dp[N - 1])
