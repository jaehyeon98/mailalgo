import sys
from collections import deque, defaultdict
read = sys.stdin.readline

N = int(read())
board = [0] * N
order = deque()
recom = int(read())
stud = list(map(int, read().split()))
counting = defaultdict(int)
index = 0
for idx in range(recom):
    if stud[idx] in counting:
        counting[stud[idx]] += 1
    else:
        if len(order) < N:
            board[index] = stud[idx]
            order.append(stud[idx])
            counting[stud[idx]] += 1
            index += 1
        else:
            min = 1001
            cand = []
            for key, value in counting.items():
                if value < min:
                    min = value
                    cand = [key]
                elif value == min:
                    cand.append(key)
            if len(cand) == 1:
                order.remove(cand[0])
                counting.pop(cand[0])
                index = board.index(cand[0])
                board[index] = stud[idx]
                order.append(stud[idx])
                counting[stud[idx]] += 1
            else:
                for i in order.copy():
                    if i in cand:
                        order.remove(i)
                        counting.pop(i)
                        index = board.index(i)
                        board[index] = stud[idx]
                        order.append(stud[idx])
                        counting[stud[idx]] += 1
                        break
order = list(order)
order.sort()
print(' '.join(map(str, order)))