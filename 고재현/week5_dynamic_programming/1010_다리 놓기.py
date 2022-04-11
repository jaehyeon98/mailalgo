# combinations으로 풀면 시간 초과
# math.factorial도 가능하대

dp = [[0]*30 for _ in range(30)]
for i in range(30):
    for j in range(30):
        if j == 1:
            dp[i][j] = i
        elif i == j:
            dp[i][j] = 1
        elif j < i:
            dp[i][j] = dp[i-1][j-1]+dp[i-1][j]

T = int(input())
for _ in range(T):
    n, m = map(int,input().split())
    print(dp[m][n])

