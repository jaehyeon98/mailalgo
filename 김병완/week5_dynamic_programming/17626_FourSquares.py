# 숫자를 하나하나 제곱수로 만들어가며 가장 최소한으로 드는 비용들을 기록한다.
import sys
read = sys.stdin.readline

N = int(read())
dp = [0, 1]

for i in range(2, N + 1):
    min_val = 0xffffff
    j = 1

    while (j ** 2) <= i:
        min_val = min(min_val, dp[i - (j ** 2)]) #전까지 만드는 최소 비용과 지금 이걸 만드는데 그 전에 값들을 비교 판단
        j += 1

    dp.append(min_val + 1)
print(dp[N])




