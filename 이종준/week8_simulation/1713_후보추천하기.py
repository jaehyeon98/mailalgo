N = int(input())
R = int(input())
data = list(map(int, input().split()))
board = [] # 사진틀
rec_list = [] # 추천수 카운팅

for i in range(R):
    if data[i] in board:
        for j in range(len(board)):
            if data[i] == board[j]:
                rec_list[j] += 1
    else:
        if len(board) >= N:
            for k in range(N):
                if rec_list[k] == min(rec_list):
                    board.pop(k)
                    rec_list.pop(k)
                    break

        board.append(data[i])
        rec_list.append(1)

board.sort()
for i in board:
    print(i, end=' ')
            