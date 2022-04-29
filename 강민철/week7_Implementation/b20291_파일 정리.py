import sys;sys.stdin = open('20291.txt')

N = int(input())

dct = dict()
for i in range(N):
    f = sys.stdin.readline().strip().split('.')
    dct[f[1]] = dct.get(f[1], 0) + 1

for c in sorted(list(dct)):
    print(c, dct[c])