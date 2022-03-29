R, C = map(int, input().split())
data = [list(input()) for _ in range(R)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

q = set()

my_str = data[0][0]
q.add((0, 0, my_str))

ans = 1
def bfs():
    global ans
    while q:
        r, c, str1 = q.pop()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < R and 0 <= nc < C and data[nr][nc] not in str1:
                q.add((nr, nc, str1 + data[nr][nc]))
                ans = max(ans, len(str1) + 1)
bfs()
print(ans)