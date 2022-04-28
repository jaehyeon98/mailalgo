S = input()
ans = ''
tmp = []
flag = False
for i in S:
    if i == '<':
        tmp.reverse()
        s = ''.join(tmp)
        ans += s
        tmp = [i]
        flag = True
    elif i == '>':
        tmp.append(i)
        ans += ''.join(tmp)
        tmp = []
        flag = False

    elif i == ' ' and not flag:
        tmp.reverse()
        tmp.append(i)
        ans += ''.join(tmp)
        tmp = []
    elif i == ' ' and flag:
        tmp.append(i)
    else:
        tmp.append(i)
tmp.reverse()
ans += ''.join(tmp)
print(ans)