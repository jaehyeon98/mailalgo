import sys;sys.stdin = open('1629.txt')

A, B, C = map(int, input().split())
arr = []

def DFS(exp, mod, s):
    if B == exp: return mod
    if exp * 2 <= B:
        arr.append(mod)
        return DFS(exp * 2, (mod*mod)%C, exp * 2)
    else:
        if len(arr) == 1:
            preMod = arr[0]
            return DFS(exp + 1, (mod * preMod) % C, s)
        else:
            x = s
            while exp + x > B:
                x /= 2
                preMod = arr.pop()
            return DFS(exp + x, (mod*preMod)%C, x)

print(DFS(1, A%C, 1))