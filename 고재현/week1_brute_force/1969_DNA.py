# 짧은 후기: 문제를 잘못 이해해서 30분동안 삽질.. 문제랑 테케를 잘 보자 제발
n, m = map(int, input().split())
lst = []
for i in range(n):
    lst.append(input())

ans = ''
hd = 0
for i in range(m):
    a, t, g, c = 0, 0, 0, 0
    for j in range(n):
        if lst[j][i] == 'A':
            a += 1
        elif lst[j][i] == 'T':
            t += 1
        elif lst[j][i] == 'G':
            g += 1
        else:
            c += 1
    if max(a,t,g,c) == a:
        ans += 'A'
        hd += (t+g+c)
    elif max(a,t,g,c) == c:
        ans += 'C'
        hd += (t + g + a)
    elif max(a,t,g,c) == g:
        ans += 'G'
        hd += (a+t+c)
    else:
        ans += 'T'
        hd += (a+g+c)

print(ans)
print(hd)


