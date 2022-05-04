from collections import deque
def check(number, max_arr):
    if number < 0:
        number = (max_arr - 1) - (((-1) * number - 1) % max_arr)
    elif n >= max_arr:
        number = number % max_arr
    return number


def first(d, s, n):
    for i in range(n):
        for j in range(n):
            if cloud[i][j] == 1:
                cloud[i][j] = 0
                ni, nj = check(i + (di[d] * s), n), check(j + (dj[d] * s), n)
                print(ni,nj)
                cloud[ni][nj] = 1


def second():
    pass


def fourth():
    pass


def fifth():
    pass


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cloud = [[0] * n for _ in range(n)]
q = deque()
q.append([[n-1,0],[n-1,1],[n-2,0],[n-2,1]])

di = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dj = [0, -1, -1, 0, 1, 1, 1, 0, -1]
wi = [1,1,-1,-1]
wj = [1,-1,-1,1]
for _ in range(m):
    d, s = map(int, input().split())
    while q:
        i,j = q.popleft()
        ni, nj = check(i + (di[d] * s), n), check(j + (dj[d] * s), n)
        arr[ni][nj] += 1
        for k in range(4):







