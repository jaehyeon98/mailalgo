import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
N, S = map(int, input().split())
cand = list(map(int, input().split()))

def dfs(s, cur_num):
    global answer
    if s >= N:
        if cur_num == S:
            answer += 1
        return
    else:
        # 선택 x
        dfs(s + 1, cur_num)
        # 선택 o
        dfs(s + 1, cur_num + cand[s])
if S == 0:
    answer = -1
else:
    answer = 0
dfs(0, 0)
print(answer)