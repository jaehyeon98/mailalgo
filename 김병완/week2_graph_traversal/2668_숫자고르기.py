import sys

input = sys.stdin.readline

N = int(input())
board = [0] * (N + 1)
for i in range(1, N + 1):
    board[i] = int(input())

def dfs(cand, target, num):
    cand.add(num)
    target.add(board[num])
    if board[num] not in cand:
        return dfs(cand, target, board[num])
    if cand == target:
        answer.update(cand)
        return

answer = set()
for i in range(1, N + 1):
    if i not in answer:
        dfs(set(), set(), i)

print(len(answer))
print('\n'.join(map(str, sorted(list(answer)))))


