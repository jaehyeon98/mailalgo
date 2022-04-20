import sys
read = sys.stdin.readline

A, B = map(int, read().split())

nums = [(A, 1)]

idx = 0
while idx < len(nums):
    now, cnt = nums[idx]
    first = now << 1
    second = now * 10 + 1
    if first <= B:
        nums.append((first, cnt + 1))
    if second <= B:
        nums.append((second, cnt + 1))
    idx += 1

for num in nums:
    if num[0] == B:
        print(num[1])
        break
else:
    print(-1)