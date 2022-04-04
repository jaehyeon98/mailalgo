n = int(input())
stair = [0] * (n+1)
for k in range(1,n+1):
    stair[k] = int(input())

if n == 1:
    print(stair[1])
elif n == 2:
    print(stair[1]+stair[2])
else:
    max_sum = [0] * (n+1)
    max_sum[1] = stair[1]
    max_sum[2] = stair[1] + stair[2]

    for i in range(3, n+1):
        max_sum[i] = max(max_sum[i-3]+stair[i-1]+stair[i], max_sum[i-2]+stair[i])

    print(max_sum[n])