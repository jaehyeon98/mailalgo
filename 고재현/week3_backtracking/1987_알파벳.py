from collections import deque
import sys
input = sys.stdin.readline
# 시간 초과의 늪에서 빠져나올 수가 없었음...
# def dfs(i,j,n):
#     global max_val
#     if max_val < n:
#         max_val = n
#     for k in range(4):
#         ni,nj = i+di[k], j+dj[k]
#         if 0 <= ni < r and 0 <= nj < c:
#             if not visit[arr[ni][nj]]:
#                 visit[arr[i][j]] = True
#                 dfs(ni,nj,n+1)
#                 visit[arr[i][j]] = False

def bfs(si,sj):
    global max_val
    q = set([(si,sj,arr[si][sj])])
    while q:
        i,j,my_str = q.pop()
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if (0 <= ni < r) and (0 <= nj < c) and (arr[ni][nj] not in my_str):
                q.add((ni,nj,my_str+arr[ni][nj]))
                max_val = max(max_val,len(my_str)+1)




r, c = map(int,input().split())
arr = list(input() for _ in range(r))
di = [1,0,-1,0]
dj = [0,1,0,-1]
max_val = 1
# visit = {'A': False, 'B': False, 'C': False, 'D': False, 'E': False, 'F': False, 'G': False, 'H': False, 'I': False,
#          'J': False, 'K': False, 'L': False, 'M': False, 'N': False, 'O': False, 'P': False, 'Q': False, 'R': False,
#          'S': False, 'T': False, 'U': False, 'V': False, 'W': False, 'X': False, 'Y': False, 'Z': False,
#          arr[0][0]: True}
# count = [[0]*c for _ in range(r)]
bfs(0,0)
print(max_val)