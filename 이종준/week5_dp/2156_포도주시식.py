n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

# [6, 10, 13, 9, 8, 1]
# 10, 13, 8, 1 => 33

dp = [0]
dp.append(data[0])
if n > 1:
    dp.append(data[0] + data[1])

for i in range(3, n + 1):
    case1 = data[i-1] + dp[i-2]
    case2 = data[i-1] + data[i-2] + dp[i-3]
    case3 = dp[i-1]
    dp.append(max(case1, case2, case3))

print(dp[n])