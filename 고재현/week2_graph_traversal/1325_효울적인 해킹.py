import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    cnt = 0
    q = deque()
    q.append(v)
    visit[v] = 1
    while q:
        nv = q.popleft()
        cnt += 1
        for i in arr[nv]:
            if visit[i] == 0:
                q.append(i)
                visit[i] = 1
    return cnt



n,m = map(int,input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    arr[b].append(a)


result = []
max_val = 0
for sv in range(1,n+1):
    visit = [0] * (n + 1)
    if arr[sv]:
        tmp = bfs(sv)
        if tmp >= max_val:
            if tmp == max_val:
                result.append(sv)
            else:
                result = []
                result.append(sv)
                max_val = tmp




print(' '.join(map(str,result)))
