import sys;sys.stdin = open('1182.txt')

N, S = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

def comb(n, r, s, lev, acc):
    if lev >= 1 and acc == S:
        global ans
        ans += 1
    if lev >= r:
        return
    for i in range(s, n):
        comb(n, r, i+1, lev+1, acc+arr[i])

comb(N, N, 0, 0, 0)

print(ans)