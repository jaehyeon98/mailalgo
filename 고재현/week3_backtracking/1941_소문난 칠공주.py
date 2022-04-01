from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline


def check(tmp):
    yeon = 0
    for a,b in tmp:
        if arr[a][b] == 'Y':
            yeon += 1
            if yeon >= 4:
                return False
    return True


def bfs(c):
    visit = [False]*7
    q = deque()
    q.append(c[0])
    visit[0] = True

    while q:
        i,j = q.popleft()
        for k in range(4):
            ni,nj = i+di[k], j+dj[k]
            if (ni,nj) in c:
                check_visit = c.index((ni,nj))
                if not visit[check_visit]:
                    q.append((ni,nj))
                    visit[check_visit] = True

    for b in visit:
        if b == False:
            return False
    return True



arr = list(input() for _ in range(5))
co = [(i,j) for i in range(5) for j in range(5)]
possible = list(combinations(co,7))
di = [1,0,-1,0]
dj = [0,1,0,-1]
ans = 0

for candidate in possible:
    if check(candidate):
        if bfs(candidate):
            ans += 1
print(ans)

