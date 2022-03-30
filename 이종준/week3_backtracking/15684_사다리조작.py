# N: 세로선, H: 가능한 가로점선, M: 가로 놓인 수
N, M, H = map(int, input().split())
if M == 0:
    print(0)
    exit(0)
arr = [[0] * (N) for _ in range(H)]

for _ in range(M):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1

# i번째줄에서 사다리 타서 i번째줄로 나오는지 체크
def check():
    for i in range(N):
        tmp = i
        for j in range(H):
            if arr[j][tmp] == 1:
                tmp += 1
            elif tmp > 0 and arr[j][tmp-1] == 1:
                tmp -= 1
        if tmp != i:
            return False
    return True

def dfs(r, c, cnt):
    global ans
    # cnt를 3 넘게 사용했으면 리턴
    if ans <= cnt:
        return
    # 체크해서 True 나오면 ans를 cnt로 바꾸고 리턴
    if check():
        ans = cnt
        return
    # cnt 가 3이면 리턴(이건 필요한건지 모르겠음)
    if cnt == 3:
        return
    for i in range(r, H):
        k = c if i == r else 0
        for j in range(k, N-1):
            # 연결선 있으면 다음줄로 건너가기
            if arr[i][j]:
                j += 1
            # 연결선 없으면 연결선 만들고 cnt 추가, 두 칸 옆으로 건너뛰기
            ## 바로 옆에 연결선 만들 수 없으므로!
            else:
                arr[i][j] = 1
                dfs(i, j + 2, cnt + 1)
                arr[i][j] = 0

ans = 4
dfs(0, 0, 0)
print(ans if ans < 4 else -1)