# heapq를 사용
# min heap을 사용하면 원소들이 항상 정렬된 상태로 추가되고 삭제되며 min heap에서 가장 작은 값은
# 언제나 인덱스 0, 즉 이진 트리의 루트에 위치한다
# 힙에 원소 추가 : heapq.heappush(리스트이름,원소)
# 힙에서 가장 작은 원소 삭제 후 리턴: heapq.heappop(리스트이름)
# 인덱스를 통해 접근도 가능
# 기존 리스트를 힙으로 변환 = heapq.heapify(리스트이름)

import heapq
n = int(input())

q = []

for i in range(n):
    start, end = map(int, input().split())
    q.append([start, end])

q.sort()

room = []
heapq.heappush(room, q[0][1])

for i in range(1, n):
    if q[i][0] < room[0]: # 현재 회의실 끝나는 시간보다 다음 회의 시작시간이 빠르면
        heapq.heappush(room, q[i][1]) # 새로운 회의실 개설
    else: # 현재 회의실에 이어서 회의 개최 가능
        heapq.heappop(room) # 새로운 회의로 시간 변경을 위해 pop후 새 시간 push
        heapq.heappush(room, q[i][1])

print(len(room))

