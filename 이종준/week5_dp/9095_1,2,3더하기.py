# 점화식 찾는 문제였음

T = int(input())
for _ in range(T):
    N = int(input())
    dp = [0, 1, 2, 4]
    if N < 4:
        print(dp[N])
    else:
        for i in range(4, N+1):
            tmp = dp[i-1] + dp[i-2] + dp[i-3]
            dp.append(tmp)
        print(dp[N])