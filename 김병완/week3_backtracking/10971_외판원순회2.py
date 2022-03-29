import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

N = int(input())
nod_info = [list(map(int, input().split())) for _ in range(N)]

visit = [False] * N

def dfs(s, now, target, cur_cost):
    global answer
    if s == N - 1:
        if now == target:
            answer = min(cur_cost, answer)
            return
    else:
        for i in range(N):
            if now == i: continue
            if visit[i]: continue
            if nod_info[now][i] == 0: continue
            next_cost = cur_cost + nod_info[now][i]
            if next_cost >= answer: continue
            visit[i] = True
            dfs(s + 1, i, target, next_cost)
            visit[i] = False

answer = 0xfffffffffff

for start in range(N):
    for nex in range(N):
        if start == nex: continue
        if nod_info[start][nex] == 0: continue
        visit[nex] = True
        dfs(0, nex, start, nod_info[start][nex])
        visit[nex] = False

print(answer)