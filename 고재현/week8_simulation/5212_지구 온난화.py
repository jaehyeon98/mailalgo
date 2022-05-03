import sys
input = sys.stdin.readline

r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
change = [[0] * c for _ in range(r)]
di = [0, 1, -1, 0]
dj = [1, 0, 0, -1]
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'X':
            cnt = 0
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < r and 0 <= nj < c:
                    if arr[ni][nj] == '.':
                        cnt += 1
                else:
                    cnt += 1
            if cnt >= 3:
                change[i][j] = 1
start_i = r - 1
start_j = c - 1
last_i = 0
last_j = 0
for i in range(r):
    for j in range(c):
        if change[i][j] == 1:
            arr[i][j] = '.'
        elif arr[i][j] == 'X':
            if start_i > i:
                start_i = i
            if start_j > j:
                start_j = j
            if last_i < i:
                last_i = i
            if last_j < j:
                last_j = j


for i in range(start_i,last_i+1):
    for j in range(start_j,last_j+1):
        print(arr[i][j],end='')
    print()
