# 아직 미해결. 시간초과
N = int(input())
arr = []
for _ in range(N):
    word = input()
    arr.append(word)

ans = []

def perm(k, leng, my_str):
    global ans
    if k == leng:
        if my_str not in ans:
            ans.append(my_str)
            print(my_str)
        return
    for i in range(leng):
        if not visited[i]:
            visited[i] = 1
            perm(k + 1, leng, my_str + tmp_word[i])
            visited[i] = 0
    

for word in arr:
    tmp_word = sorted(word)
    visited = [0] * len(word)
    perm(0, len(word), '')

# for i in ans:
#     print(i)