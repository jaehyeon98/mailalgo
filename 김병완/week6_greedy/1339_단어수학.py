import sys

read = sys.stdin.readline

N = int(read())
words = [read().rstrip() for _ in range(N)]

letters = dict()
for word in words:
    length = len(word)
    for i in range(length - 1, -1, -1):
        letters[word[i]] = max(length - i, letters[word[i]])