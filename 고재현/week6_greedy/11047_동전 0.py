# pypy로는 맞지만 python으로는 시간초과
# import sys
# input = sys.stdin.readline
#
# n, k = map(int,input().split())
# arr = [0] * n
# for i in range(n):
#     arr[i] = int(input())
#
# cnt = 0
# for i in range(n-1,-1,-1):
#     if k <= 0:
#         break
#     if k < arr[i]:
#         continue
#     while k >= arr[i]:
#         cnt += 1
#         k -= arr[i]
#
# print(cnt)


import sys
input = sys.stdin.readline

n, k = map(int,input().split())
arr = [0] * n
for i in range(n):
    arr[i] = int(input())

cnt = 0
for i in range(n-1,-1,-1):
    if k <= 0:
        break
    if k < arr[i]:
        continue
    cnt += k // arr[i]
    k = k % arr[i]

print(cnt)
