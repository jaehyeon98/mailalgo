N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N - 1 and j == N - 1:
            break
        nr = i + data[i][j]
        nc = j + data[i][j]
        if nr < N:
            dp[nr][j] += dp[i][j]
        if nc < N:
            dp[i][nc] += dp[i][j]

print(dp[N-1][N-1])