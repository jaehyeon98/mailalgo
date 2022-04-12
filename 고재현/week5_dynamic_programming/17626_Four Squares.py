# 어려움,, 넘 어려움,,
# 갱장히 어려움
n = int(input())
d = [0] * (n + 1)
d[0], d[1] = 0, 1

for i in range(2, n + 1):
    minValue = 1e9
    j = 1
    while (j ** 2) <= i:
        minValue = min(minValue, d[i - (j ** 2)])
        j += 1
    d[i] = minValue + 1

print(d[n])
