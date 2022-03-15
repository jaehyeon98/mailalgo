import sys;sys.stdin = open('1969.txt')

N, M = map(int, input().split())
arr = [input() for _ in range(N)]
cnt = [[0]*4 for _ in range(M)]
alph = ['A', 'C', 'G', 'T']

for dna in arr:
    for i in range(M):
        for j in range(4):
            if dna[i] == alph[j]:
                cnt[i][j] += 1

DNA = ''
ans = 0

for w in cnt:
    maxi = max(w)
    flag = False
    for i in range(4):
        if w[i] == maxi and not flag:
            flag = True
            DNA += alph[i]
            continue
        ans += w[i]

print(DNA)
print(ans)