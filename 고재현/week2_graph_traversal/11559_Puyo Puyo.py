def dfs(i,j):
    visit[i][j] = True
    for k in range(4):
        ni,nj = i + di[k], j+dj[k]
        if 0<=ni<12 and 0<=nj<=6:
            if not visit[ni][nj] and puyo[ni][nj] == puyo[si][sj]:


puyo = [list(input()) for _ in range(12)]
visit = [[False]*6 for _ in range(12)]
di = [1,0,-1,0]
dj = [0,1,0,-1]

for si in range(11):
    for sj in range(6):
        if puyo[si][sj] != '.' and visit[si][sj] == False:
            dfs(si,sj)