N = int(input())
data = [input() for _ in range(N)]
word_dict = {}
num_list = []
for i in range(N):
    for j in range(len(data[i])):
        if data[i][j] in word_dict:
            word_dict[data[i][j]] += 10**(len(data[i])-j-1)
        else:
            word_dict[data[i][j]] = 10**(len(data[i])-j-1)

for value in word_dict.values():
    num_list.append(value)

num_list.sort(reverse=True)

i = 9
for j in range(len(num_list)):
    num_list[j] = num_list[j] * i
    i -= 1
print(sum(num_list))