C = int(input())

def perm(k):
    global ans
    global pick
    if k == 11:
        tmp = sum(pick)
        ans = max(ans, tmp)
        return
    for i in range(11):
        if not visited[i] and data[k][i] != 0:
            visited[i] = 1
            pick.append(data[k][i])
            perm(k+1)
            visited[i] = 0
            pick.pop()

for tc in range(C):
    data = [list(map(int, input().split())) for _ in range(11)]
    visited = [0] * 11
    pick = []
    ans = 0
    perm(0)
    print(ans)