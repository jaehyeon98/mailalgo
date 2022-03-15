import sys;sys.stdin = open('2422.txt')

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
used = [0] * (N+1)

ans = 0
def comb(n, r, s, lev):
    if lev >= r:
        global ans
        ans += 1
        return
    for i in range(s, n+1):
        if used[i]: continue
        used[i] += 1
        for j in arr[i]:
            used[j] += 1
        comb(n, r, i+1, lev+1)
        used[i] -= 1
        for j in arr[i]:
            used[j] -= 1

comb(N, 3, 1, 0)
print(ans)