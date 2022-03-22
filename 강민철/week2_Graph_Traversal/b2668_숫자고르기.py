import sys;sys.stdin = open('2668.txt')

N = int(input())
arr = [0] * (N+1)
for i in range(1, N+1):
    arr[i] = int(input())

ansSet = set()

def DFS(n, s, v, st):
    st.add(n)
    x = arr[n]
    if x == s:
        return v
    if x not in st:
        return DFS(x, s, v+1, st)
    st.discard(n)
    return 0

cnt = 0
for i in range(1, N+1):
    if i in ansSet: continue
    tempSet = set()
    tmp = DFS(i, i, 1, tempSet)
    if not tmp: continue
    cnt += tmp
    ansSet |= tempSet

print(cnt)
ans = sorted(list(ansSet))
for i in ans:
    print(i)