R, C = map(int, input().split())
data = [["."] * (C + 2)]
for _ in range(R):
    data.append(["."] + list(input()) + ["."])
data.append(["."] * (C + 2))
fifty_years = [[""] * (C + 2) for _ in range(R + 2)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

min_r = 20
max_r = 0
min_c = 20
max_c = 0

for i in range(R+2):
    for j in range(C+2):
        if data[i][j] == "X":
            cnt = 0
            for k in range(4):
                nr = i + dr[k]
                nc = j + dc[k]
                if data[nr][nc] == '.':
                    cnt += 1
            if cnt >= 3:
                fifty_years[i][j] = '.'
            else:
                fifty_years[i][j] = 'X'
                if i < min_r:
                    min_r = i
                if i > max_r:
                    max_r = i
                if j < min_c:
                    min_c = j
                if j > max_c:
                    max_c = j
        else:
            fifty_years[i][j] = '.'

for i in range(min_r, max_r + 1):
    for j in range(min_c, max_c + 1):
        print(fifty_years[i][j], end='')
    print()