import sys;sys.stdin = open('1010.txt')

def fac(n):
    if n <= 1: return 1
    return n * fac(n-1)

def solve():
    N, M = map(int, input().split())
    if not N or not M: return 0
    return int(fac(M) / (fac(M-N) * fac(N)))

for tc in range(int(input())):
    print(solve())