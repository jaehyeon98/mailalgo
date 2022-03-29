import sys;sys.stdin = open('1759.txt')

L, C = map(int, input().split())
arr = input().split()
arr.sort()
lst = []

def comb(n, r, s, lev):
    if lev >= r:
        tmp = set(lst)
        if len(tmp & {'a', 'e', 'i', 'o', 'u'}) >= 1 and len(tmp-{'a', 'e', 'i', 'o', 'u'}) >= 2:
            print(''.join(lst))
        return
    for i in range(s, n-r+1+lev):
        lst.append(arr[i])
        comb(n, r, i+1, lev+1)
        lst.pop()

comb(C, L, 0, 0)