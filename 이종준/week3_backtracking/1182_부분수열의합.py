N, S = map(int, input().split())
data = list(map(int, input().split()))

def func(s, k, M):
    global ans
    if k == M:
        if sum(pick) == S:
            ans += 1
        return
    for i in range(s, N):
        pick.append(data[i])
        func(i + 1, k + 1, M)
        pick.pop()

ans = 0
for i in range(1, N + 1):
    pick = []
    func(0, 0, i)

print(ans)