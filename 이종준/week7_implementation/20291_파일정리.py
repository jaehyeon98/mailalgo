N = int(input())
data = [input() for _ in range(N)]

ans_dict = {}

for word in data:
    tmp_length = len(word)
    idx = 0
    for i in range(tmp_length):
        if word[i] == '.':
            idx = i
            break
    my_ext = word[idx+1:tmp_length]
    if not my_ext in ans_dict:
        ans_dict[my_ext] = 1
    else:
        ans_dict[my_ext] += 1

ans = sorted(ans_dict.items())
ans1 = dict(ans)

for key, value in ans1.items():
    print(key, value)