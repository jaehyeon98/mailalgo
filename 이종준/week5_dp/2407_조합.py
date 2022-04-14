N, M = map(int, input().split())
tmp1 = 1
for i in range(N, N-M, -1):
    tmp1 *= i
tmp2 = 1
for i in range(1, M + 1):
    tmp2 *= i

print(tmp1 // tmp2)
