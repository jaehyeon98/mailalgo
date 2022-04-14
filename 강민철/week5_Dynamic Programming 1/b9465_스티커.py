import sys;sys.stdin = open('9465.txt')

for tc in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]

    if n == 1:
        print(max(arr[0][0], arr[1][0]))
    elif n == 2:
        print(max(arr[0][0] + arr[1][1], arr[0][1] + arr[1][0]))
    else:
        arr[0][1] += arr[1][0]
        arr[1][1] += arr[0][0]
        for i in range(2, n):
            arr[0][i] = max(max(arr[0][i-2], arr[1][i-2]), arr[1][i-1]) + arr[0][i]
            arr[1][i] = max(max(arr[0][i-2], arr[1][i-2]), arr[0][i-1]) + arr[1][i]
        print(max(arr[0][n-1], arr[1][n-1]))