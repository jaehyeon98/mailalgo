S = input()
T = input()

# breaker = False
# for item in product_list:
#     tmp = S
#     for i in item:
#         if i == 0:
#             tmp += 'A'
#         elif i == 1:
#             tmp += 'B'
#             tmp = tmp[::-1]
#     if tmp == T:
#         breaker = True
#         break

# if breaker:
#     print(1)
# else:
#     print(0)

# T에서 제거해 나가는 방법
def dfs(t):
    if len(t) == len(S):
        if t == S:
            print(1)
            exit(0)
        return
    if t[0] == 'B':
        t = t[::-1]
        t = t[:-1]
        dfs(t)
        t += 'B'
        t = t[::-1]

    if t[-1] == 'A':
        t = t[:-1]
        dfs(t)
        t += 'A'

dfs(T)
print(0)
