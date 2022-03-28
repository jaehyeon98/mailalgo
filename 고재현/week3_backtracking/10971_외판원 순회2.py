def back(i):
    if i == n:
        print(tmp)
        return

    if not visit[i]:
        tmp.append(i)
        visit[i] = True
        back(i+1)
        visit[i] = False
        tmp.pop()


n = int(input())
visit = [False] * n
tmp = []
arr = [list(map(int,input().split())) for _ in range(n)]
min1 = 1000000000
back(0)