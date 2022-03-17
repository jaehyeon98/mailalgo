# pypy보다 python이 더 빠르네?
def perm(a,b):
    global k
    global max_val
    if a == b:
        ans1 = int(''.join(ans))
        if ans1 > n:
            return
        if ans1 > max_val:
            max_val = ans1
        elif ans1 < max_val:
            return

    else:
        for i in range(k-1,-1,-1):
            ans.append(lst[i])
            perm(a,b+1)
            ans.pop()


n, k = map(int,input().split())
lst = list(input().split())
l = len(str(n))
ans = []
max_val = 0
for i in range(l,0,-1):
    perm(i,0)
print(max_val)




        


