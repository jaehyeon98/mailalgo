import sys;sys.stdin = open('16928.txt')
from collections import deque

def solve():
    N, M = map(int, input().split())
    ladder = dict()
    snake = dict()
    for _ in range(N):
        x, y = map(int, input().split())
        ladder[x] = y
    for _ in range(M):
        u, v = map(int, input().split())
        snake[u] = v

    visited = 0
    cnt = 0
    dq = deque()
    dq.append(1)
    visited |= 1<<1
    while dq:
        cnt += 1
        for _ in range(len(dq)):
            n = dq.popleft()
            for i in range(1, 7):
                nxt = n + i
                if nxt > 100: continue
                if nxt == 100: return cnt
                if ladder.get(nxt) and not visited & 1<<nxt:
                    dq.append(ladder[nxt])
                    visited |= 1<<ladder.get(nxt)
                elif snake.get(nxt) and not visited & 1<<nxt:
                    dq.append(snake[nxt])
                    visited |= 1<<snake.get(nxt)
                elif not visited & 1<<nxt:
                    dq.append(nxt)

                visited |= 1<<nxt

print(solve())