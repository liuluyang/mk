#coding:utf8


A = "aabtchj"
B = "sghkrt"
S = "asahgbktrchjt"

def static(A, B, S):
    if len(A+B) != len(S):  # 首先判断 两个的长度，是否相同。
        return False
    a = len(A)+1
    b = len(B)+1

    li = [[[] for _ in range(a)] for _ in range(b)]
    li[0][0] = True
    for i in range(1, a):
        li[0][i] = li[0][i-1] and A[i-1] == S[i-1]

    for j in range(1, b):
        li[j][0] = li[j-1][0] and B[j-1] == S[j-1]

    for i in range(1, a):
        for j in range(1, b):
            li[j][i] = (li[j][i-1] and A[i-1] == S[i+j-1]) or (li[j-1][i] and B[j-1] == S[i+j-1])
    for n in li:
        print(n)
    return li[j][i]

print("static", static(A, B, S))