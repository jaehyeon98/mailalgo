# 중복순열로 풀기
from itertools import product

N, K = map(int, input().split())

k_list = list(map(str, input().split()))

len_N = len(str(N))

while True:
    product_list = list(product(k_list, repeat=len_N))
    tmp_list = []
    for item in product_list:
        tmp = int(''.join(item))
        if N >= tmp:
            tmp_list.append(tmp)
    if len(tmp_list):
        print(max(tmp_list))
        break
    else:
        len_N -= 1