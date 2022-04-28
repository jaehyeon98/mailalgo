import sys
read = sys.stdin.readline

strings = read().rstrip()
length = len(strings)
result = []
stack = []
idx = 0
while idx < length:
    if strings[idx] == ' ':
        while stack:
            result.append(stack.pop())
        result.append(' ')
        idx += 1
    elif strings[idx] == "<":
        while stack:
            result.append(stack.pop())
        while strings[idx] != ">":
            result.append(strings[idx])
            idx += 1
        result.append(strings[idx])
        idx += 1
    else:
        stack.append(strings[idx])
        idx += 1

while stack:
    result.append(stack.pop())

print(''.join(result))
