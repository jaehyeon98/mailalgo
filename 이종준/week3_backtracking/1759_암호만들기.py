L, C = map(int, input().split())
data = list(input().split())
data.sort()
pick = []
vowel = ['a', 'e', 'i', 'o', 'u']
ans = []
def comb(s, k):
    global ans
    if k == L:
        # 0: 모음, 1: 자음
        tmp = [0] * 2
        for j in pick:
            if j in vowel:
                tmp[0] += 1
            else:
                tmp[1] += 1
        if tmp[0] >= 1 and tmp[1] >= 2:
            ans.append(''.join(pick))
        return
    for i in range(s, C):
        pick.append(data[i])
        comb(i + 1, k + 1)
        pick.pop()

comb(0, 0)
for i in ans:
    print(i)