def back(v):
    global max1
    if v == n:
        sum1 = 0
        for k in range(1,n):
            sum1 += abs(tmp[k-1]-tmp[k])
        if sum1 > max1:
            max1 = sum1
        return
    for i in range(n):
        if not visit[i]:
            visit[i]=True
            tmp.append(arr[i])
            back(v+1)
            visit[i] = False
            tmp.pop()


n = int(input())
arr = list(map(int,input().split()))
visit = [False] * n
tmp = []
max1 = -1
back(0)
print(max1)