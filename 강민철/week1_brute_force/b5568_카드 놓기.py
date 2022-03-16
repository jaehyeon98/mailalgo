import sys;sys.stdin = open('5568.txt')

N = int(input())
K = int(input())
arr = [input() for _ in range(N)]
ans = set()
used = [0] * N

def perm(n, r, lev, c):
    if lev >= r:
        ans.add(c)
        return
    for i in range(n):
        if used[i]: continue
        used[i] = 1
        perm(n, r, lev+1, c+arr[i])
        used[i] = 0

perm(N, K, 0, '')
print(len(ans))