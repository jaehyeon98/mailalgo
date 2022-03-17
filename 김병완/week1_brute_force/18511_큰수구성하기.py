import sys
sys.stdin = open('18511.txt', 'r')
from itertools import product
input = sys.stdin.readline

N, K = input().split()
nums = input().split()

def converter(tup):
    sol = 0
    for tmp in range(len(tup) - 1, -1, -1):
        sol = sol * 10 + int(tup[tmp])
    return sol


answer = -1
compare = int(N)
for length in range(len(N), 0, -1):
    candidate = list(product(nums, repeat=length))
    tmp = []
    for cand in candidate:
        tmp.append(converter(cand))
    tmp.sort(reverse=True)
    for t in tmp:
        if t <= compare:
            answer = t
            break
    if answer != -1:
        break

print(answer)