n = int(input())
arr = list(map(int,input().split()))

arr.sort()

sum_val = 0
for i in range(n):
    tmp = 0
    for j in range(i+1):
        tmp += arr[j]
    sum_val += tmp

print(sum_val)

