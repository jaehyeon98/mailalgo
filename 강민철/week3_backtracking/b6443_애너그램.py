# 시간초과...
import sys;sys.stdin = open('6443.txt')

N = int(input())

def perm(n, r, lev):
    if lev >= r:
        result = ''.join(res)
        if result in visited: return
        visited.add(result)
        print(result)
        return
    for i in range(n):
        if used[i]: continue
        used[i] = 1
        res[lev] = word[i]
        perm(n, r, lev+1)
        used[i] = 0

for tc in range(N):
    word = list(input())
    word.sort()
    visited = set()
    L = len(word)
    used = [0] * L
    res = [0] * L

    perm(L, L, 0)