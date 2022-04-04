N = int(input())

def solve():
    memo = [0] * (N+2)
    memo[1] = 1
    memo[2] = 3
    if N < 3: return memo[N]
    for i in range(3, N+1):
        memo[i] = (memo[i-1] + memo[i-2] * 2) % 10007
    return memo[N]

print(solve())