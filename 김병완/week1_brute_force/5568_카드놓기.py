import sys
from itertools import permutations
sys.stdin = open('5568_카드놓기.txt', 'r')

input = sys.stdin.readline

N = int(input())
K = int(input())

comb = []
for _ in range(N):
    comb.append(input().rstrip())

answer = set()
settings = permutations(comb, K)
for setting in settings:
    answer.add(''.join(setting))

print(len(answer))


