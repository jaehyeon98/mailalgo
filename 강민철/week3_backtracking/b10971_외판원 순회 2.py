import sys;sys.stdin = open('10971.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [0] * N
ans = 1000000*N

def DFS(s, p, acc, lev):
    global ans
    if lev >= N:
        if not arr[p][s]: return # 시작 부분으로 돌아갈 수 있는지 판단을 해줘야지!
        acc += arr[p][s]
        if acc < ans:
            ans = acc
        return
    if acc >= ans:
        return
    for i in range(N):
        if visited[i]: continue
        if not arr[p][i]: continue
        visited[i] = 1
        DFS(s, i, acc+arr[p][i], lev+1)
        visited[i] = 0

for i in range(N):
    visited[i] = 1
    DFS(i, i, 0, 1)
    visited[i] = 0

print(ans)