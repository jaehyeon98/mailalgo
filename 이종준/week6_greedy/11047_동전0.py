N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

ans = 0

for i in range(N-1, -1, -1):
    if coins[i] > K:
        continue
    ans += (K // coins[i])
    K = K % coins[i]

print(ans)