import sys
from collections import defaultdict
read = sys.stdin.readline

extends = defaultdict(int)
keys = []
N = int(read())

for _ in range(N):
    tmp = read().rstrip().split('.')
    extends[tmp[1]] += 1

for key in extends:
    keys.append(key)

keys.sort()

for k in keys:
    print(k + ' ' + str(extends[k]))
