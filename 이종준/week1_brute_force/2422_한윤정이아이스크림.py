import sys
input = sys.stdin.readline

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(M)]

arr = [[0] * (N + 1) for _ in range(N + 1)]
for i in data:
    r, c = i[0], i[1]
    arr[r][c] = 1
    arr[c][r] = 1

ans = 0

for i in range(1, N+1):
    for j in range(i + 1, N+1):
        for k in range(j + 1, N+1):
            if not arr[i][j] and not arr[i][k] and not arr[j][k]:
                ans += 1

print(ans)