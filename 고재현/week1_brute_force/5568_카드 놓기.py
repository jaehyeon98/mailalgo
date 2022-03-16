from itertools import permutations
n = int(input())
k = int(input())
arr = []
for i in range(n):
    tmp = input()
    arr.append(tmp)

num = []
card = set(list(permutations(arr,k)))
for c in card:
    sum1 = ''
    for n in c:
        sum1 += n
    num.append(sum1)

print(len(set(num)))
