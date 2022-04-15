n = int(input())
arr = list(map(int,input().split()))
dp = [1] * n
# 나보다 작은 애들 중 최대인 것에 +1
for i in range(1,n):
    max_val = 0
    for j in range(0,i):
        if arr[j] < arr[i]:
            max_val = max(max_val,dp[j])

    dp[i] = max_val + 1

print(max(dp))