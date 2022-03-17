from itertools import permutations

N = int(input())
K = int(input())
num_list = []
for _ in range(N):
    a = input()
    num_list.append(a)

my_set = set()

for comb in list(permutations(num_list, K)):
    tmp = []
    for i in comb:
        tmp.append(i)
    my_set.add(''.join(tmp))

print(len(my_set))