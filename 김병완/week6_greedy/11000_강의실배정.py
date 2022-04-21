import sys
from heapq import heapify, heappop, heappush
read = sys.stdin.readline

N = int(read())
times = [tuple(map(int, read().split())) for _ in range(N)]

times.sort()

rooms = []
heappush(rooms, times[0][1])

for i in range(1, N):
    if times[i][0] < rooms[0]:
        heappush(rooms, times[i][1])
    else:
        heappop(rooms)
        heappush(rooms, times[i][1])

print(len(rooms))