import sys
read = sys.stdin.readline

N = int(read())
times = list(map(int, read().split()))

times.sort()

result = 0
for i in range(N, -1, -1):
    result += sum(times[:i])

print(result)