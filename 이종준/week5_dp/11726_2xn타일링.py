N = int(input())
dp = [0, 1, 2]
if N < 3:
    print(dp[N] % 10007)
else:
    for i in range(3, N + 1):
        tmp = dp[i-1] + dp[i - 2]
        dp.append(tmp)
    print(dp[N] % 10007)