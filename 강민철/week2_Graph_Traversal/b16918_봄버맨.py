import sys;sys.stdin = open('16918.txt')

R, C, N = map(int, input().split())
stack = []
arr = [[0]*C for _ in range(R)]
for i in range(R):
    row = input()
    for j in range(C):
        if row[j] == '.': continue
        arr[i][j] = 2

di, dj = (1, -1, 0, 0), (0, 0, 1, -1)
for t in range(1, N):
    if t & 1:
        for i in range(R):
            for j in range(C):
                if arr[i][j] == 2:
                    arr[i][j] -= 1
                    stack.append((i, j))
                elif arr[i][j] == 0: arr[i][j] = 3
    else:
        while stack:
            i, j = stack.pop()
            arr[i][j] = 0
            for d in range(4):
                ni, nj = i + di[d], j + dj[d]
                if ni < 0 or ni >= R or nj < 0 or nj >= C: continue
                arr[ni][nj] = 0
        for i in range(R):
            for j in range(C):
                if arr[i][j] != 3: continue
                arr[i][j] -= 1

for i in range(R):
    for j in range(C):
        if arr[i][j]: arr[i][j] = 'O'
        else: arr[i][j] = '.'

for i in arr:
    print(*i, sep='')