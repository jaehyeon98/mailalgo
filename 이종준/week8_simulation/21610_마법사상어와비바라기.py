from collections import deque

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

dr = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dc = [0, -1, -1, 0, 1, 1, 1, 0, -1]

# 대각
ddr = [-1, -1, 1, 1]
ddc = [-1, 1, 1, -1]

move_list = [list(map(int, input().split()))  for _ in range(M)]
clouds = [[0] * N for _ in range(N)]
clouds[N-2][0] = 1
clouds[N-2][1] = 1
clouds[N-1][0] = 1
clouds[N-1][1] = 1

q = deque()
q.append((N-2, 0))
q.append((N-2, 1))
q.append((N-1, 0))
q.append((N-1, 1))

def bfs(d, s):
    global clouds, cloud_idx
    while q:
        r, c = q.popleft()
        # 이동이 마이너스일때는 바꿔줘야 함 => 금요일에 해야지 ㅎㅎ
        nr = (r + dr[d] * s) % N
        nc = (c + dc[d] * s) % N
        clouds[r][c] = 0
        clouds[nr][nc] = 1
        data[nr][nc] += 1
        cloud_idx.append((nr, nc))
          
cnt = 0
while cnt < M:
    d, s = move_list[cnt]
    cloud_idx = []
    bfs(d, s)
    print(clouds)
    for r, c in cloud_idx:
        tmp = 0
        for i in range(4):
            nnr = r + ddr[i]
            nnc = c + ddc[i]
            if 0 <= nnr < N and 0 <= nnc < N and data[nnr][nnc] != 0:
                tmp += 1
        data[r][c] += tmp
    
    for i in range(N):
        for j in range(N):
            if clouds[i][j] == 0 and data[i][j] >= 2:
                clouds[i][j] = 1
                data[i][j] -= 2
                q.append((i, j))
            elif clouds[i] != 0:
                clouds[i][j] = 0
    
    cnt += 1