import sys
input = sys.stdin.readline

n = int(input())
nums = [0] + list(map(int, input().split()))
dp = [-1001] * (n + 1)

for i in range(1, n + 1):
    dp[i] = max(nums[i], dp[i - 1] + nums[i])
print(max(dp))