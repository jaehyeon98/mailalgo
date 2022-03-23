def dfs(v):
    visit[v] = True
    for nv in arr[v]:
        if not visit[nv]:
            dfs(nv)
        else:
            ans.append(nv)

n = int(input())
arr = [[] for _ in range(n+1)]
for i in range(1,n+1):
    arr[i].append(int(input()))

ans = []
for i in range(1,n+1):
    visit = [False] * (n+1)
    dfs(i)

tmp = set(ans)
result = sorted(list(tmp))
print(len(result))
for i in result:
    print(i)
