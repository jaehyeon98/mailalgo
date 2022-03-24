import sys;sys.stdin = open('11559.txt')
from collections import deque

arr = [[0] * 6 for _ in range(12)]
for i in range(12):
    row = input()
    for j in range(6):
        if row[j] == 'R':
            arr[i][j] = 1
        elif row[j] == 'G':
            arr[i][j] = 2
        elif row[j] == 'B':
            arr[i][j] = 3
        elif row[j] == 'P':
            arr[i][j] = 4
        elif row[j] == 'Y':
            arr[i][j] = 5

ans = 0
visited = [[0] * 6 for _ in range(12)]
dq1 = deque()
dq2 = deque()
dq3 = deque()
di, dj = (1, -1, 0, 0), (0, 0, 1, -1)
def turn2(i, j, cnt):
    dq1.append((i, j))
    dq2.append((i, j))
    visited[i][j] = 1
    cnt += 1
    while dq1:
        i, j = dq1.popleft()
        for d in range(4):
            ni, nj = i+di[d], j+dj[d]
            if ni < 0 or ni >= 12 or nj < 0 or nj >= 6 or visited[ni][nj] or arr[ni][nj] != arr[i][j]: continue
            dq1.append((ni, nj))
            dq2.append((ni, nj))
            visited[ni][nj] = 1
            cnt += 1
    if cnt < 4:
        dq2.clear()
    else:
        while dq2:
            dq3.append(dq2.popleft())

def turn3():
    for j in range(6):
        for i in range(11, -1, -1):
            if arr[i][j]:
                y, x = i, j
                while y+1 < 12 and not arr[y+1][x]:
                    arr[y+1][x] = arr[y][x]
                    arr[y][x] = 0
                    y += 1

def turn1():
    global visited
    visited = [[0] * 6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if arr[i][j] and not visited[i][j]:
                turn2(i, j, 0)
    if dq3:
        global ans
        ans += 1
        while dq3:
            i, j = dq3.popleft()
            arr[i][j] = 0
        turn3()
        turn1()

turn1()
print(ans)