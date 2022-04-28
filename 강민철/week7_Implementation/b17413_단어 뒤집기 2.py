import sys;sys.stdin = open('17413.txt')

words = input()

arr = []
idx = 0
flag = False
for i in range(len(words)):
    if flag:
        if words[i] == '>':
            arr.append(words[idx:i+1])
            idx = i+1
            flag = False
        continue
    if words[i] == '<':
        flag = True
        arr.append(words[idx:i][::-1])
        idx = i
        continue
    if words[i] == ' ':
        arr.append(words[idx:i][::-1])
        arr.append(' ')
        idx = i+1
        continue
    if i == len(words)-1:
        arr.append(words[idx:i+1][::-1])

print(''.join(arr))