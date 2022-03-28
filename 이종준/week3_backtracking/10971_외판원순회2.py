N = int(input())
data = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    tmp = list(map(int, input().split()))
    for j in range(N):
        data[i][j+1] = tmp[j]

visited = [0] * (N + 1)

def func(s):
    visited[s] = 1
    for e in range(1, N + 1):
        if data[s][e] and not visited[e]:
            func(e)
            visited[e] = 0

for i in range(1, N + 1):
    func(i)
