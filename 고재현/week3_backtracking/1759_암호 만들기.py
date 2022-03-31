def back(n,depth):
    if depth == l:
        a = 0 # 모음
        b = 0 # 자음
        for word in tmp:
            if word in v:
                a += 1
            else:
                b+= 1
        if a >= 1 and b >= 2:
            ans.append(''.join(tmp))
        return

    for i in range(n,c):
        tmp.append(words[i])
        back(i+1,depth+1)
        tmp.pop()



l, c = map(int,input().split())
words_tmp = list(input().split())
words = sorted(words_tmp)
tmp = []
ans = []
v = ['a', 'e', 'i', 'o', 'u']
back(0,0)
for an in ans:
    print(an)