a, b = map(int,input().split())
cnt = 0
while a < b :

    if b % 10 == 1:
        b = b // 10
        cnt += 1
    elif b % 2 == 0:
        b = b // 2
        cnt += 1
    else:
        b = -1

if b == a:
    print(cnt+1)
else:
    print(-1)
