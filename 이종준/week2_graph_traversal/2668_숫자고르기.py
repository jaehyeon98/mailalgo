N = int(input())

arr = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
    j = int(input())
    arr[i].append(j)

def dfs(s):    
    tmp1.append(s)
    visited[s] = 1
    for e in arr[s]:
        if not visited[e]:
            visited[e] = 1
            tmp2.append(e)
            dfs(e)
        else:
            tmp2.append(e)
            return

ans_list = set()

for i in range(1, N + 1):
    visited = [0] * (N + 1)
    tmp1 = []
    tmp2 = []
    dfs(i)
    if sorted(tmp1) == sorted(tmp2):
        for j in range(len(tmp1)):
            ans_list.add(tmp1[j])

result = list(ans_list)
result.sort()

print(len(result))
for i in range(len(result)):
    print(result[i])