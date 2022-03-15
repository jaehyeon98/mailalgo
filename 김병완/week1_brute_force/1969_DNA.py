# sys는 import하고 쓰는거다
import sys; sys.stdin = open('김병완_1969_DNA.txt', 'r')

input = sys.stdin.readline

N, M = map(int, input().split())
DNAset = []

for _ in range(N):
    DNAset.append(input().rstrip())

min_HD = 0
answer = []
for idx in range(M):
    weight = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    DNA = ''
    for j in range(N):
        weight[DNAset[j][idx]] += 1
    DNA = max(weight.keys(), key=(lambda k: weight[k]))
    answer.append(DNA)
    min_HD += (N - weight[DNA])

print(''.join(answer))
print(min_HD)