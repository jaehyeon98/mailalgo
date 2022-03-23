import sys

input = sys.stdin.readline

def dfs(s, n):
    global answer, answer_list
    if s == n:
        for idx in range(N):
            if cVisit[idx]:
                if not tVisit[cVisit[idx]]:
                    break
        else:
            answer = n
            answer_list = cVisit[:]
    else:
        for cd in candi:
            if tVisit[board[cd]]: continue
            cVisit[cd] = True
            tVisit[board[cd]] = True
            dfs(s + 1, n)
            cVisit[cd] = False
            tVisit[board[cd]] = False

N = int(input())
board = [0] * N
for i in range(N):
    board[i] = int(input())
candi = set(board)
length = len(candi)
print(length)
cVisit = [False] * N
tVisit = [False] * N
answer = -1
answer_list = []
for i in range(length, 0, -1):
    dfs(0, i)
    if answer != -1:
        break
print(answer, answer_list)
