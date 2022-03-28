def back(i,sum1): # i는 다음 더할 인덱스, sum1은 지금까지 더한 합
    global ans
    if i >= n:
        return
    sum1 += arr[i]

    if sum1 == s:
        ans +=1

    back(i+1,sum1)
    back(i+1,sum1-arr[i])


n, s = map(int,input().split())
arr = list(map(int,input().split()))
ans = 0
back(0,0)
print(ans)