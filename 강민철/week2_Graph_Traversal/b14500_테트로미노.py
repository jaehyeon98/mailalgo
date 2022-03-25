import sys;sys.stdin = open('14500.txt')

N, M = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def rotate(arr):
    lst = [[] for _ in range(len(arr[0]))]
    Y = len(arr)
    X = len(arr[0])
    for i in range(Y):
        for j in range(X):
            lst[j].append(arr[Y-1-i][j])
    return lst

def sym(arr):
    lst = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            lst[i][j] = arr[i][M-1-j]
    return lst

def shape1(i, j):
    return [(i, j), (i, j+1), (i, j+2), (i, j+3)]

def shape2(i, j):
    return [(i, j), (i, j+1), (i+1, j), (i+1, j+1)]

def shape3(i, j):
    return [(i, j), (i, j+1), (i, j+2), (i+1, j+1)]

def shape4(i, j):
    return [(i, j), (i+1, j), (i+1, j+1), (i+2, j+1)]

def shape5(i, j):
    return [(i, j), (i+1, j), (i+2, j), (i+2, j+1)]

def pro(func, i, j, arr):
    cnt = 0
    LY = len(arr)
    LX = len(arr[0])
    for y, x in func(i, j):
        if y < 0 or y >= LY or x < 0 or x >= LX:
            return 0
        cnt += arr[y][x]
    return cnt

def solve(arr):
    maxi = 0
    LY = len(arr)
    LX = len(arr[0])
    for i in range(LY):
        for j in range(LX):
            n = pro(shape1, i, j, arr)
            if n > maxi:
                maxi = n
            n = pro(shape2, i, j, arr)
            if n > maxi:
                maxi = n
            n = pro(shape3, i, j, arr)
            if n > maxi:
                maxi = n
            n = pro(shape4, i, j, arr)
            if n > maxi:
                maxi = n
            n = pro(shape5, i, j, arr)
            if n > maxi:
                maxi = n
    return maxi

def solve2(arr):
    maxi = 0
    LY = len(arr)
    LX = len(arr[0])
    for i in range(LY):
        for j in range(LX):
            n = pro(shape4, i, j, arr)
            if n > maxi:
                maxi = n
            n = pro(shape5, i, j, arr)
            if n > maxi:
                maxi = n
    return maxi

maximum = 0
maximum = max(maximum, solve(arr))
tmp = rotate(arr)
maximum = max(maximum, solve(tmp))
tmp = rotate(tmp)
maximum = max(maximum, solve(tmp))
tmp = rotate(tmp)
maximum = max(maximum, solve(tmp))
tmp = sym(arr)
maximum = max(maximum, solve2(tmp))
tmp = rotate(tmp)
maximum = max(maximum, solve2(tmp))
tmp = rotate(tmp)
maximum = max(maximum, solve2(tmp))
tmp = rotate(tmp)
maximum = max(maximum, solve2(tmp))

print(maximum)