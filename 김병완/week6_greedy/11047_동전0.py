import sys
read = sys.stdin.readline

N, K = map(int, read().split())
kinds = []

for _ in range(N):
    tmp = int(read())
    if tmp > K: continue
    kinds.append(tmp)

kinds.sort(reverse=True)

cnt = 0
for kind in kinds:
    if K >= kind:
        cnt += K // kind
        K = K % kind

print(cnt)

