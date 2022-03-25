import sys
from collections import deque
input = sys.stdin.readline

def bfs(sv):
    q = deque()
    q.append(sv)
    visit[sv] = 0
    while q:
        v = q.popleft()
        for k in range(1,7):
            nv = v+k
            if nv <= 100:
                # 만약 가려는 칸이 뱀이나 사다리 칸이면
                if nv in move:
                    nv = move[nv]
                if not visit[nv]:
                    q.append(nv)
                    visit[nv] = visit[v] + 1


n, m = map(int,input().split())

move = dict()
for _ in range(n+m):
    a,b = map(int,input().split())
    move[a] = b

visit = [0] * 101
bfs(1)

print(visit[100])