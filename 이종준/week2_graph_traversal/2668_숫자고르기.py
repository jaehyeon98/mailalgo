N = int(input())
# data = [[0] * N for _ in range(2)]
# for i in range(N):
#     data[0][i] = i + 1
#     data[1][i] = int(input())

arr = [[] for _ in range(N + 1)]

for i in range(N):
    j = int(input())
    arr[i + 1].append(j)



def dfs(s):    
    tmp1.append(s)
    for e in arr[s]:
        if visited[e] != 1:
            visited[e] += 1
            tmp2.append(e)
            dfs(e)

ans = 0
ans_list = []

for i in range(1, N + 1):
    visited = [0] * (N + 1)
    tmp1 = []
    tmp2 = []
    dfs(i)
    print(tmp1)
    print(tmp2)
    if sorted(tmp1) == sorted(tmp2):
        ans = len(tmp1)
        ans_list = tmp2

print(ans)
for i in range(ans):
    print(ans_list[i])