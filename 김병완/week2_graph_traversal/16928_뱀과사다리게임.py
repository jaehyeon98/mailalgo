# BFS는 visit 없으면 메모리초과 뜬다
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
Sn_La = [i for i in range(100)]

for _ in range(N):
    Ls, Le = map(int, input().split())
    Ls -= 1
    Le -= 1
    Sn_La[Ls] = Le

for _ in range(M):
    Ss, Se = map(int, input().split())
    Ss -= 1
    Se -= 1
    Sn_La[Ss] = Se
visit = [False] * 100
q = deque([(0, 0)])
visit[0] = True
answer = 0
while q:
    flag = False
    now, cnt = q.popleft()
    for i in range(1, 7):
        if now + i >= 100: continue
        nex = Sn_La[now + i]
        if visit[nex]: continue
        if nex == 99:
            flag = True
            answer = cnt + 1
            break
        visit[nex] = True
        q.append((nex, cnt + 1))
    if flag:
        break

print(answer)
