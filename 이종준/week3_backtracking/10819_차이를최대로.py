N = int(input())
arr = list(map(int, input().split()))
pick = []
visited = [0] * N
ans = 0

def func(k):
    global ans
    if k == N:
        tmp = 0
        for i in range(N-1):
            tmp += abs(pick[i] - pick[i+1])
        if ans < tmp:
            ans = tmp
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            pick.append(arr[i])
            func(k + 1)
            visited[i] = 0
            pick.pop()

func(0)

print(ans)