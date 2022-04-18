N = int(input())
data = list(map(int, input().split()))

data.sort()

for i in range(1, N):
    data[i] += data[i-1]
print(sum(data))