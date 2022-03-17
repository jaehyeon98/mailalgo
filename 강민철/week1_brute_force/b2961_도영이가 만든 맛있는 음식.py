import sys;sys.stdin = open('2961.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = abs(arr[0][0] - arr[0][1])

def comb(n, s, lst):
    if lst:
        global ans
        S, B = 1, 0
        for i in lst:
            S *= i[0]
            B += i[1]
        if ans > abs(S-B):
            ans = abs(S-B)
    for i in range(s, n):
        comb(n, i+1, lst+[arr[i]])

comb(N, 0, [])
print(ans)