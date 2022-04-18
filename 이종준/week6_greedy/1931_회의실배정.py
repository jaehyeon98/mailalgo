N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
data.sort(key=lambda x:x[0])

data.sort(key=lambda x:x[1])

ans = 0
last_time = 0

for i in range(N):
    if data[i][0] >= last_time:
        ans += 1
        last_time = data[i][1]

print(ans)
