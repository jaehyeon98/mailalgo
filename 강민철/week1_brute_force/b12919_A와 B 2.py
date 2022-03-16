import sys;sys.stdin = open('12919.txt')

S = input()
T = input()

def solve(t, r, lev):
    if t == S:
        return 1
    if lev >= r:
        return
    if t[-1] == 'A':
        if solve(t[:len(t)-1], r, lev+1): return 1
    if t[0] == 'B':
        if solve(t[1:][::-1], r, lev+1): return 1
    return 0

print(solve(T, len(T)-len(S), 0))