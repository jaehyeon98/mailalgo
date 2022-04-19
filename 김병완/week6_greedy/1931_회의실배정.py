import sys

read = sys.stdin.readline

N = int(read())

times = []
for _ in range(N):
    times.append(list(map(int, read().split())))

times.sort(key=lambda k: (k[1], k[0]))

result = 1
idx = 0
while idx < N:
    ending = times[idx][1]
    for i in range(idx + 1, N):
        if ending <= times[i][0]:
            idx = i
            result += 1
            break
    else:
        idx = N

print(result)
