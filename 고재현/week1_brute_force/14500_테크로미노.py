def dfs(i,j,move):
    if move == 4:
        sum1
        return
    if 0 <= i < n and 0 <= j < m:
        if visit[i][j] == 0:
            sum1 +=
            visit[i][j] = 1
            for k in range(4):
                dfs(i+di[k], j+dj[k],move+1)


n, m = map(int(input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]
visit = [[0]*m for _ in range(n)]
sum1 = 0
di = [1,0,-1,0]
dj = [0,1,0,-1]