# 현재 자신을 선택하지 않는 경우도 고려해야 함
n = int(input())
arr = [0] * 10000
for i in range(n):
    arr[i] = int(input())
dp = [0] * 10000
dp[0] = arr[0]
dp[1] = arr[0]+arr[1]
dp[2] = max(arr[0]+arr[1],arr[1]+arr[2], arr[0]+arr[2])
for i in range(3,n):
    dp[i] = max(arr[i]+dp[i-2], arr[i]+arr[i-1]+dp[i-3], dp[i-1])

print(dp[n-1])