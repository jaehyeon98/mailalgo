N = int(input())
dp = [0, 1]
for i in range(2, N + 1):
    if i % 2 == 0:
        tmp = dp[i-1] * 2 + 1
        dp.append(tmp)
    else:
        tmp = dp[i-1] * 2 - 1
        dp.append(tmp)

print(dp[N] % 10007)