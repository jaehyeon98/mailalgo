n = int(input())
dic = {}
for _ in range(n):
    file = input()
    for i in range(len(file)):
        if file[i] == ".":
            dot = i

    text = file[dot+1:]
    if text in dic:
        dic[text] += 1
    else:
        dic[text] = 1
for i in sorted(dic):
    print(i,dic[i])





