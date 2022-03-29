def back(now,d,sum):
    global min1
    if min1 < sum:
        return
    if d == n:
        if arr[now][0] == 0:
            return
        sum += arr[now][0]
        if min1 > sum:
            min1 = sum
        return
    visit[now] = True
    for i in range(1,n):
        if not visit[i] and arr[now][i] != 0:
            sum += arr[now][i]
            back(i,d+1,sum)
            sum -= arr[now][i]

    visit[now] = False


n = int(input())
visit = [False] * n
arr = [list(map(int, input().split())) for _ in range(n)]
min1 = 9876543210
for i in range(n):
    back(i,1,0)
print(min1)