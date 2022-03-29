import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
visit = [False] * N
answer = 0
def dfs(s, now, cur_num):
    global answer
    if s == N - 1:
        answer = max(answer, cur_num)
        return
    else:
        for i in range(N):
            if visit[i]: continue
            nex = cur_num + abs(nums[now] - nums[i])
            visit[i] = True
            dfs(s + 1, i, nex)
            visit[i] = False

for start in range(N):
    visit[start] = True
    dfs(0, start, 0)
    visit[start] = False

print(answer)

