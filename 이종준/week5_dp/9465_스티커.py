T = int(input())
for _ in range(T):
    n = int(input())
    data = [list(map(int, input().split())) for __ in range(2)]
    
    dp = [[0] * n for __ in range(2)]
    dp[0][0] = data[0][0]
    dp[1][0] = data[1][0]

    for j in range(1, n):
        for i in range(2):
            if i == 0:
                if j - 2 >= 0:
                    dp[i][j] = data[0][j] + max(dp[1][j-1], dp[1][j-2])
                    
                else:
                    dp[i][j] = data[0][j] + dp[1][j-1]
                    
            if i == 1:
                if j - 2 >= 0:
                    dp[i][j] = data[1][j] + max(dp[0][j-1], dp[0][j-2])
                    
                else:
                    dp[i][j] = data[1][j] + dp[0][j-1]
                   

    print(max(dp[0][n-1], dp[1][n-1]))