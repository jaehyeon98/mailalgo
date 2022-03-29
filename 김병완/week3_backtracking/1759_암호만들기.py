import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

L, C = map(int, input().split())

codes = input().split()
vowels = {'a', 'e', 'i', 'o', 'u'}
visit = [False] * C
answer = set()

def dfs(s, cur_str, v, c):
    if L - s <= 1:
        if v < 1: return
    elif L - s <= 2:
        if c < 2: return
    if s == L:
        answer.add(''.join(sorted(cur_str)))
        return
    else:
        for i in range(C):
            if visit[i]: continue
            if codes[i] in vowels:
                nv = v + 1
                nc = c
            else:
                nv = v
                nc = c + 1

            visit[i] = True
            nex_str = cur_str[:]
            nex_str.append(codes[i])
            dfs(s + 1, nex_str, nv, nc)
            visit[i] = False


dfs(0, [], 0, 0)
result = sorted(answer)
print('\n'.join(result))

