import sys

read = sys.stdin.readline

N, M, R = map(int, read().split())

board = [list(map(int, read().split())) for _ in range(N)]
visit = [[False] * M for _ in range(N)]
tmp = []