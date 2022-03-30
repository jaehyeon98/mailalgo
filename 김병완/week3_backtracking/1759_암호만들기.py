import sys
sys.setrecursionlimit(10 ** 8)
from itertools import combinations
input = sys.stdin.readline

L, C = map(int, input().split())

codes = input().split()
codes.sort()
vowels = {'a', 'e', 'i', 'o', 'u'}
answer = []

# def dfs(s, cur_str, v, c):
#     if s >= C : return
#     if len(cur_str) == L:
#         if v >= 1 and c >= 2:
#             answer.append(''.join(sorted(cur_str)))
#         return
#     else:
#         nv = v
#         nc = c
#         if codes[s] in vowels:
#             nv += 1
#         else:
#             nc += 1
#         nex_str = cur_str[:]
#         nex_str.append(codes[s])
#         dfs(s + 1, nex_str, nv, nc)
#         dfs(s + 1, cur_str, v, c)

candidates = list(combinations(codes, L))
# print(candidates)
for candidate in candidates:
    vc = [0] * 2
    for string in candidate:
        if string in vowels:
            vc[0] += 1
        else:
            vc[1] += 1
    if vc[0] >= 1 and vc[1] >= 2:
        answer.append(''.join(candidate))


# dfs(0, [], 0, 0)
# result = sorted(answer)
print('\n'.join(answer))

