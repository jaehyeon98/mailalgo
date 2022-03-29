N = int(input())
data = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    tmp = list(map(int, input().split()))
    for j in range(N):
        data[i][j+1] = tmp[j]

def func(s, cnt, my_sum, origin):   
    global ans
    if cnt == N:
        if data[s][origin]:
            if ans > my_sum + data[s][origin]:
                ans = my_sum + data[s][origin]
        return    
    for e in range(1, N + 1):
        if data[s][e] and not visited[e] and e != origin:
            visited[e] = 1
            func(e, cnt + 1, my_sum + data[s][e], origin)
            visited[e] = 0        

ans = 9876543210

for i in range(1, N + 1):
    visited = [0] * (N + 1)
    visited[i] = 1
    func(i, 1, 0, i)

print(ans)