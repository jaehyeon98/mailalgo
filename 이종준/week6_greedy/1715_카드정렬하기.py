import sys
import heapq

input = sys.stdin.readline
heap = []
N = int(input())
for _ in range(N):
    heapq.heappush(heap, int(input()))

if len(heap) == 1:
    print(0)
else:
    ans = 0
    while len(heap) > 1:
        min1 = heapq.heappop(heap)
        min2 = heapq.heappop(heap)
        tmp_sum = min1 + min2
        ans += tmp_sum
        heapq.heappush(heap, tmp_sum)
    print(ans)