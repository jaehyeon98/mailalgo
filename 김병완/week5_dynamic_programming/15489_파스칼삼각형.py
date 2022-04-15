import sys

read = sys.stdin.readline

def fact(n):
    tmp = 1
    for i in range(1, n + 1):
        tmp *= i
    return tmp

def combi(n, r):
    result = fact(n) / (fact(n - r) * fact(r))
    return int(result)

R, C, W = map(int, read().split())
R -= 1
C -= 1
result = 0
for w in range(W):
    for k in range(w + 1):
        result += combi(R + w, C + k)

print(result)