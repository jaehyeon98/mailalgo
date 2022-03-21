from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    arr[B].append(A)

q = deque()

def bfs():
    tmp = 0
    while q:
        s = q.popleft()
        tmp += 1
        for e in arr[s]:
            if not visited[e]:
                q.append(e)
                visited[e] = 1
    return tmp

ans = 0
ans_list = []

for i in range(1, N + 1):
    visited = [0] * (N + 1)
    visited[i] = 1
    q.append(i)
    tmp_ans = bfs()
    if tmp_ans >= ans:
        ans_list.append(i)
    if tmp_ans > ans:
        ans = tmp_ans
        ans_list = []
        ans_list.append(i)

print(*ans_list)