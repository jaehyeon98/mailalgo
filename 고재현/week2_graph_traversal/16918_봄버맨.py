def bomb():
    for i in range(r):
        for j in range(c):
            if bomb[i][j] == 3:
                bomb[i][j] = -1
                for k in range(4):
                    ni, nj = i+di[k], j+dj[k]
                    if 0<= ni < r and 0<= nj < c:
                        bomb[ni][nj] = -1


def add():
    for i in range(r):
        for j in range(c):
            if bomb[i][j] == -1:
                bomb[i][j] = 0


r,c,n = map(int,input().split())
arr = [list(input()) for _ in range(r)]
bomb = [[-1] * c for _ in range(r)]

di = [1,-1,0,0]
dj = [0,0,1,-1]

#1초
for si in range(r):
    for sj in range(c):
        if arr[si][sj] == 'O':
            bomb[si][sj] = 1



#2초
for i in range(r):
    for j in range(c):
        if bomb[i][j] == -1:
            bomb[i][j] = 0
        else:
            bomb[i][j] += 1


#3초 이후
flag = False
for time in range(3,n+1):

    if flag:
        flag = False
        for i in range(r):
            for j in range(c):
                if bomb[i][j] == -1:
                    bomb[i][j] = 0


    for i in range(r):
        for j in range(c):

            # 폭탄이 설치되어 있는 곳에
            if bomb[i][j] != -1:
                bomb[i][j] += 1
                if bomb[i][j] == 3:
                    flag = True
                    bomb[i][j] = -1
                    for k in range(4):
                        ni,nj = i+di[k], j+dj[k]
                        if 0 <=ni<r and 0<=nj<c:
                            bomb[ni][nj] = -1


for i in range(r):
    for j in range(c):
        if bomb[i][j] == -1:
            arr[i][j] = '.'
        else:
            arr[i][j] = 'O'

for i in range(r):
    for j in range(c):
        print(arr[i][j], end='')
    print()



