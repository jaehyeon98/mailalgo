import sys
input = sys.stdin.readline
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
            min_val = 10001
            index_val = 101
            for k in range(len(picture)):
                if vote[k] < min_val:
                    min_val = vote[k]
                    index_val = k
            del picture[index_val]
            del vote[index_val]
            picture.append(arr[i])
            vote.append(1)

        else:
            picture.append(arr[i])
            vote.append(1)


print(*sorted(picture))
