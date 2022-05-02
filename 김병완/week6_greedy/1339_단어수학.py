import sys
from collections import defaultdict
read = sys.stdin.readline

N = int(read())
words = [read().rstrip() for _ in range(N)]

letters = defaultdict(int)
for word in words:
    length = len(word)
    for i in range(length - 1, -1, -1):
        letters[word[i]] += 10 ** (length - i - 1)

cnt = [letters[letter] for letter in letters]
cnt.sort(reverse=True)
total = 0
for i in range(len(cnt)):
    total += cnt[i] * (9 - i)

print(total)