n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

dp[arr[0][0]][0] = 1
dp[0][arr[0][0]] = 1
for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            continue
        if i+arr[i][j] < n:
            dp[i+arr[i][j]][j] += dp[i][j]
        if j+arr[i][j] < n:
            dp[i][j+arr[i][j]] += dp[i][j]


print(dp[n-1][n-1])
