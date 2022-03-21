import sys;sys.stdin = open('2178.txt')
from collections import deque

def solve():
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    visited = [[0]*M for _ in range(N)]

    dq = deque()
    dq.append((0, 0))
    visited[0][0] = 1

    di = (1, -1, 0, 0)
    dj = (0, 0, 1, -1)
    while dq:
        i, j = dq.popleft()
        for d in range(4):
            ni, nj = i+di[d], j+dj[d]
            if ni < 0 or ni >= N or nj < 0 or nj >= M or visited[ni][nj] or arr[ni][nj] == '0': continue
            dq.append((ni, nj))
            visited[ni][nj] = visited[i][j]+1
            if ni == N-1 and nj == M-1: return visited[ni][nj]

print(solve())