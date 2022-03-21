from collections import deque
def bfs(i,j):
    q = deque()
    q.append((i,j))
    visit[i][j] = 1
    while q:
        i,j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m:
                if arr[ni][nj] == 1 and visit[ni][nj] == 0:
                    visit[ni][nj] = visit[i][j] + 1
                    q.append((ni,nj))

    return visit[n-1][m-1]

n,m = map(int,input().split())
arr = [list(map(int,input())) for _ in range(n)]
visit = [[0] * m for _ in range(n)]
di = [0,1,0,-1]
dj = [1,0,-1,0]
ans = bfs(0,0)
print(ans)