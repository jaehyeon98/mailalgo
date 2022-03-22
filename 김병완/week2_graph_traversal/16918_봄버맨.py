import sys
sys.stdin = open('16918.txt', 'r')
input = sys.stdin.readline

def convert(li):
    tmp = []
    for i in range(R):
        tmp.append(''.join(li[i]))
    return '\n'.join(tmp)

R, C, N = map(int, input().split())
Case1 = [list(input().rstrip()) for _ in range(R)]
Case2 = [['O'] * C for _ in range(R)]
Case3 = [['O'] * C for _ in range(R)]
Case4 = [['O'] * C for _ in range(R)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for r in range(R):
    for c in range(C):
        if Case1[r][c] == 'O':
            Case3[r][c] = '.'
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if nr < 0 or nr >= R or nc < 0 or nc >= C: continue
                Case3[nr][nc] = '.'

for r in range(R):
    for c in range(C):
        if Case3[r][c] == 'O':
            Case4[r][c] = '.'
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if nr < 0 or nr >= R or nc < 0 or nc >= C: continue
                Case4[nr][nc] = '.'

if N == 1:
    print(convert(Case1))
elif N % 4 == 1:
    print(convert(Case4))
elif N % 2 == 0:
    print(convert(Case2))
elif N % 4 == 3:
    print(convert(Case3))

