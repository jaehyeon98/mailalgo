from collections import deque

data = [list(input()) for _ in range(12)]

q = deque()

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs():
    global tmp_list
    cnt = 1
    while q:
        r, c, clr = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < 12 and 0 <= nc < 6 and not visited[nr][nc] and data[nr][nc] == clr:
                q.append((nr, nc, clr))
                tmp_list.append((nr, nc))
                visited[nr][nc] = 1
                cnt += 1
    return cnt

ans = 0

while True:
    visited = [[0] * 6 for _ in range(12)]
    flag = False
    for i in range(12):
        for j in range(6):
            if data[i][j] != '.' and not visited[i][j]:
                tmp_list = [(i, j)]
                q.append((i, j, data[i][j]))
                visited[i][j] = 1
                if bfs() >= 4:
                    flag = True
                    for tmp in tmp_list:
                        data[tmp[0]][tmp[1]] = '.'
    if flag == False:
        break
    else:
        for i in range(6):
            for j in range(11, 0, -1):
                if data[j][i] == '.':
                    for k in range(j - 1, -1, -1):
                        if data[k][i] != '.':
                            data[j][i] = data[k][i]
                            data[k][i] = '.'
                            break
        ans += 1

print(ans)