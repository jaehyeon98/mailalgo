from collections import deque

R, C, N = map(int, input().split())

data = [list(input()) for _ in range(R)]

q = deque()

my_timer = 1

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs():
    while q:
        r, c = q.popleft()
        data[r][c] = '.'
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < R and 0 <= nc < C:
                data[nr][nc] = '.'

for i in range(R):
    for j in range(C):
        if data[i][j] == 'O':
            q.append((i, j))

if N == 1:
    for i in range(R):
        for j in range(C):
            print(data[i][j], end="")
        print()
else:
    while my_timer < N:
        my_timer += 1
        if my_timer % 2 == 0:
            for i in range(R):
                for j in range(C):
                    if data[i][j] == '.':
                        data[i][j] = 'O'            
        else:
            bfs()
            for i in range(R):
                for j in range(C):
                    if data[i][j] == 'O':
                        q.append((i, j))
    
    for i in range(R):
        for j in range(C):
            print(data[i][j], end="")
        print()
