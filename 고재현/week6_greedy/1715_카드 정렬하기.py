import heapq
n = int(input())
arr =[]
for _ in range(n):
    heapq.heappush(arr,int(input()))
sum_val = 0
while len(arr) >= 2 :
    tmp = heapq.heappop(arr) + heapq.heappop(arr)
    sum_val += tmp
    heapq.heappush(arr,tmp)

print(sum_val)


