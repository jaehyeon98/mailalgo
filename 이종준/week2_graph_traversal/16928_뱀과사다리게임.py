from collections import deque

N, M = map(int, input().split())

board_cnt = [0] * 101

adj = [0] * 101

for _ in range(N + M):
    s, e = map(int, input().split())
    adj[s] = e

q = deque()

visited = [0] * 101

def bfs():
    global board_cnt
    while q:
        s = q.popleft()
        if s == 100:
            return
        for i in range(1, 7):
            ns = s + i
            if 0 < ns <= 100 and not visited[ns]:
                if adj[ns]:
                    ns = adj[ns]
                if not visited[ns]:
                    visited[ns] = 1
                    q.append(ns)
                    board_cnt[ns] = board_cnt[s] + 1

q.append(1)
visited[1] = 1
bfs()
print(board_cnt[-1])