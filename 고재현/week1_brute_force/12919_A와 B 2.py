# 질문 검색에서 얻어낸 힌트 : 더하려고 하지 말고 반대로 생각해라
def check(t,n,l):
    global flag
    if t == s:
        flag = 1
        return
    # 첫번째 경우
    elif n < l:
        return
    if t[-1] == 'A':
        check(t[:len(t)-1],n,l+1)

    if t[0] == 'B':
        check(t[::-1][:len(t)-1],n,l+1)



s = input()
t = input()
d = len(t) - len(s)
flag = 0
check(t,len(t)-len(s),0)
print(flag)


# 시간 초과 방법
# def check(a,n):
#     global s
#     global flag
#     if a == n:
#         if s == t:
#             flag = 1
#             return
#         else:
#             return
#     elif a > n:
#         return
#     else:
#         s += 'A'
#         check(a+1,n)
#         s.pop()
#
#         s += 'B'
#         s = s[::-1]
#         check(a+1,n)
#         s = s[::-1]
#         s.pop()
#
#
#
# s = list(input())
# t = list(input())
# n = len(t)
# flag = 0
# ans = s
# check(len(s),n)
# print(flag)
