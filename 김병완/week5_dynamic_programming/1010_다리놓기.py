import sys
read = sys.stdin.readline

def fact(n):
    if n == 0 or n == 1:
        return 1
    answer = 1
    for i in range(1, n + 1):
        answer *= i
    return answer

for tc in range(int(read())):
    N, M = map(int, read().split())
    result = int(fact(M) / (fact((M - N)) * fact(N)))
    print(result)