import sys;sys.stdin = open('18511.txt')

N, K = map(int, input().split())
arr = input().split()
numSet = set()

def perm(n, lev, c):
    if int(c) > N:
        return
    numSet.add(int(c))
    for i in range(n):
        perm(n, lev+1, c+arr[i])

perm(K, 0, '0')

print(max(numSet))