A, B = map(int, input().split())

ans = 1
while True:
    if B == A:break
    if A > B or (B % 10 != 1 and B % 2 != 0):
        ans = -1
        break
    else:
        if B % 10 == 1:
            B = B // 10
            ans += 1
        else:
            B = B // 2
            ans += 1
print(ans)