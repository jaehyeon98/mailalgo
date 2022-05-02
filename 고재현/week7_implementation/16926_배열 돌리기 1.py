import sys
input = sys.stdin.readline

n,m,r = map(int,input().split())

data = [list(map(int,input().split())) for _ in range(n)]

for _ in range(r):
    for i in range(min(n, m) // 2):

        x, y = i, i
        temp = data[x][y]

        for j in range(i + 1, n - i):
            x = j
            prev_value = data[x][y]
            data[x][y] = temp
            temp = prev_value

        for j in range(i + 1, m - i):
            y = j
            prev_value = data[x][y]
            data[x][y] = temp
            temp = prev_value

        for j in range(i + 1, n - i):
            x = n - j - 1
            prev_value = data[x][y]
            data[x][y] = temp
            temp = prev_value

        for j in range(i + 1, m - i):
            y = m - j -1
            prev_value = data[x][y]
            data[x][y] = temp
            temp = prev_value

for i in range(n):
    for j in range(m):
        print(data[i][j], end=' ')
    print()