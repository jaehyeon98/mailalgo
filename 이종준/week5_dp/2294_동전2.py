N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))
dp = [0] * (K + 1)

for i in range(1, K + 1):
    tmp = []
    for coin in coins:
        if coin <= i and dp[i-coin] != -1:
            tmp.append(dp[i-coin])    
    if not tmp:
        dp[i] = -1
    else:
        dp[i] = min(tmp) + 1

print(dp[K])