import sys
from collections import deque
sys.stdin = open('1325.txt', 'r')

input = sys.stdin.readline

N, M = map(int, input().split())
rels = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    rels[b].append(a)

maximum = 0
answer = []

for i in range(N):
    visit = [False] * N
    q = deque()
    q.append(i)
    visit[i] = True
    cnt = 1
    while q:
        now = q.popleft()
        for n in rels[now]:
            if visit[n]: continue
            visit[n] = True
            q.append(n)
            cnt += 1
    if maximum < cnt:
        answer = [i + 1]
        maximum = cnt
    elif maximum == cnt:
        answer.append(i + 1)

print(*answer)