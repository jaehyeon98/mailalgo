import sys
import heapq

input = sys.stdin.readline

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

heap = []

data.sort(key=lambda x:x[0])
heapq.heappush(heap, data[0][1])

for i in range(1, N):
    if data[i][0] >= heap[0]:
        heapq.heappop(heap)
        heapq.heappush(heap, data[i][1])
    else:
        heapq.heappush(heap, data[i][1])

print(len(heap))