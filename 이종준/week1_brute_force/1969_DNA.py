N, M = map(int, input().split())
data = [input() for _ in range(N)]

hamming_distance = [0] * M

for i in range(M):
    nucleo = [0] * 4 # A T G C
    for j in range(N):
        if data[j][i] == 'A':
            nucleo[0] += 1
        elif data[j][i] == "T":
            nucleo[3] += 1
        elif data[j][i] == "G":
            nucleo[2] += 1
        elif data[j][i] == "C":
            nucleo[1] += 1
    for k in range(4):
        if nucleo[k] == max(nucleo):
            hamming_distance[i] = k
            break

ans_list = []
for i in range(M):
    if hamming_distance[i] == 0:
        ans_list.append('A')
    elif hamming_distance[i] == 3:
        ans_list.append('T')
    elif hamming_distance[i] == 2:
        ans_list.append('G')
    elif hamming_distance[i] == 1:
        ans_list.append('C')

ans = 0
for i in range(M):
    for j in range(N):
        if ans_list[i] != data[j][i]:
            ans += 1

# 출력
for i in range(M):
    print(ans_list[i], end="")
print()
print(ans)
