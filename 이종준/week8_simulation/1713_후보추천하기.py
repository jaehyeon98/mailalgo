N = int(input())
R = int(input())
data = list(map(int, input().split()))
board = []
rec_list = [0] * (R + 1)

# for i in range(N + 1, R + 1):
#     if data[i] in board:
#         rec_list[data[i]] += 1
#     else:
