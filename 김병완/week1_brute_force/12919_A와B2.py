import sys
sys.stdin = open('12919.txt', 'r')

input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())
flag = False

def dfs(T):
    global flag
    if len(T) == len(S):
        if T == S:
            flag = True
        return

    if T[0] == "B":
        T = T[::-1]
        T.pop()
        dfs(T)
        T.append("B")
        T = T[::-1]
    if T[-1] == "A":
        T.pop()
        dfs(T)
        T.append("A")

dfs(T)
if flag:
    print(1)
else:
    print(0)







