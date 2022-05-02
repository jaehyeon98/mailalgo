n = int(input())
s = int(input())
arr = list(map(int,input().split()))

picture = []
vote = []
for i in range(s):
    if arr[i] in picture: # 이미 추천 받은 학생이면
        vote[picture.index(arr[i])] += 1
    else: # 새롭게 추천 받은 학생이면
        if len(picture) >= n:
            min_val = 0
            index_val = 101
            for k in range(len(picture)):
                if vote[k] < min_val:
                    min_val = vote[k]
                    index_val = k
            picture[index_val] = arr[i]
            vote[index_val] = 1
        else:
            picture.append(arr[i])
            vote.append(1)

print(picture)
print(vote)