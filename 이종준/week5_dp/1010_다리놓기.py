T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    ans = 1
    for i in range(M, M - N, -1):
        ans *= i
    tmp = 1
    for i in range(1, N + 1):
        tmp *= i

    print(int(ans / tmp))     