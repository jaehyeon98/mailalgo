import sys

sys.stdin = open('김병완_2422_한윤정.txt', 'r')

input = sys.stdin.readline

N, M = map(int, input().split())
bad = [[False] * N for _ in range(N)]
for _ in range(M):
    tmp1, tmp2 = map(int, input().split())
    tmp1 -= 1
    tmp2 -= 1
    bad[tmp1][tmp2] = True
    bad[tmp2][tmp1] = True

answer = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if not bad[i][j] and not bad[j][k] and not bad[k][i]:
                answer += 1

print(answer)



