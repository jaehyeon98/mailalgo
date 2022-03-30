import sys;sys.stdin = open('1987.txt')

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
maxi = 1

def bfsBySet():
    q = set()
    q.add((0, 0, 1<<ord(arr[0][0]), 1))

    di, dj = (1, -1, 0, 0), (0, 0, 1, -1)
    while q:
        i, j, visited, cnt = q.pop()
        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            if ni < 0 or ni >= R or nj < 0 or nj >= C or visited & 1<<ord(arr[ni][nj]): continue
            q.add((ni, nj, visited | 1<<ord(arr[ni][nj]), cnt+1))
            global maxi
            maxi = max(maxi, cnt+1)

bfsBySet()
print(maxi)