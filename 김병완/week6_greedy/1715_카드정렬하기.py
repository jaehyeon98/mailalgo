import sys
from heapq import heapify, heappush, heappop
read = sys.stdin.readline

N = int(read())

cards = [int(read()) for _ in range(N)]

heapify(cards)

result = 0
while len(cards) > 1:
    first = heappop(cards)
    second = heappop(cards)
    tmp = first + second
    result += tmp
    heappush(cards, tmp)

print(result)