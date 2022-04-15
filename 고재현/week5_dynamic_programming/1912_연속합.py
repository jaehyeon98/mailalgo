n = int(input())
arr = list(map(int,input().split()))
for i in range(1,n):
    if arr[i-1] < 0:
        arr[i] = max(arr[i-1]+arr[i],arr[i])
    else:
        arr[i] += arr[i-1]

print(max(arr))