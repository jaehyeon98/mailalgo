import sys;sys.stdin = open('1325.txt')
from collections import deque

N, M = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    arr[B].append(A)

def BFS(n):
    dq = deque()
    visited = [0] * (N+1)
    dq.append(n)
    visited[n] = 1
    acc = 1
    while dq:
        x = dq.popleft()
        for i in arr[x]:
            if visited[i]: continue
            dq.append(i)
            visited[i] = 1
            acc += 1
    return acc

memo = [0] * (N+1)
for n in range(1, N+1):
    memo[n] = BFS(n)

ans = []
maxi = 0
for n in range(1, N+1):
    if memo[n] > maxi:
        ans = [n]
        maxi = memo[n]
    elif memo[n] == maxi:
        ans.append(n)

print(*ans)