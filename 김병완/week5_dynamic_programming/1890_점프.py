import sys
read = sys.stdin.readline

N = int(read())
board = [list(map(int, read().split())) for _ in range(N)]
print(board)