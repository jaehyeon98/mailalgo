import sys;sys.stdin = open('5212.txt')

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
res = [['X'] * C for _ in range(R)]

def check(i, j):
    n = 0
    di, dj = (1, -1, 0, 0), (0, 0, 1, -1)
    for d in range(4):
        ni, nj = i+di[d], j+dj[d]
        if ni < 0 or ni >= R or nj < 0 or nj >= C:
            n += 1
            continue
        if arr[ni][nj] == '.':
            n += 1
    if n >= 3:
        return True
    return False

def solve():
    for i in range(R):
        for j in range(C):
            if arr[i][j] == '.':
                res[i][j] = '.'
                continue
            if check(i, j):
                res[i][j] = '.'

    minR = maxR = maxC = 0
    minC = C
    for i in range(R):
        if 'X' in res[i]:
            minR = i
            break

    for i in range(minR, R):
        if 'X' in res[i]:
            maxR = i

    for i in range(minR, maxR+1):
        for j in range(C):
            if res[i][j] == 'X' and j < minC:
                minC = j
            if res[i][j] == 'X' and j > maxC:
                maxC = j

    ans = []
    for i in range(minR, maxR+1):
        ans.append(res[i][minC:maxC+1])
    return ans

ans = solve()
for i in range(len(ans)):
    print(*ans[i], sep='')