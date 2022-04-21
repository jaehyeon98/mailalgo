N = int(input())

ans = 0

tmp = N % 5

if N == 1 or N == 3:
    print(-1)
else:
    if tmp % 2 == 0:
        print(N // 5 + tmp // 2)
    else:
        print((N // 5 - 1) + (tmp + 5) // 2)