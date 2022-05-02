S = list(input())

idx = 0
start = 0

while idx < len(S):
    if S[idx] == '<':
        idx += 1
        while S[idx] != ">":
            idx += 1
        idx += 1
    elif S[idx].isalnum(): # isalnum() = 문자열이 알파벳 혹은 숫자인지(boolean값 반환)
        start = idx
        while idx < len(S) and S[idx].isalnum():
            idx += 1
        tmp = S[start:idx]
        tmp.reverse()
        S[start:idx] = tmp
    else:
        idx += 1

print("".join(S))
