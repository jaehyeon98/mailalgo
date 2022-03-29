import sys;sys.stdin = open('10819.txt')

N = int(input())
arr = list(map(int, input().split()))
used = [0] * N
lst = [0] * N
maxi = 0

def solve(lst, L):
    acc = 0
    for i in range(L-1):
        acc += abs(lst[i]-lst[i+1])
    return acc

def perm(n, r, lev):
    if lev >= r:
        global maxi
        tmp = solve(lst, N)
        if tmp > maxi:
            maxi = tmp
        return
    for i in range(n):
        if used[i]: continue
        used[i] = 1
        lst[lev] = arr[i]
        perm(n, r, lev+1)
        used[i] = 0

perm(N, N, 0)
print(maxi)