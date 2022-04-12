# python3 시간초과, pypy3 통과

n = int(input())
dp = [0] * (n + 1)
dp[0] = 0
dp[1] = 1
for i in range(2, n + 1):
    tmp = 987654321
    j = 1
    while (j ** 2) <= i:
        tmp = min(tmp, dp[i-(j**2)])
        j += 1
    dp[i] = tmp + 1

print(dp[n])