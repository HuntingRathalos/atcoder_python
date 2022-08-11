# # 先頭の”a”の方が多いことを考慮できていなかった
# def judge(S):
#     if S == S[::-1]:
#         return True

#     while S[-1] == "a":
#         S = "a" + S
#         if  S == S[::-1]:
#             return True
#     return False

# S = input()
# print("Yes" if judge(S) else "No")

def judge():
    S = input()
    l = len(S) - len(S.lstrip('a'))  # 先頭の連続数
    r = len(S) - len(S.rstrip('a'))  # 末尾の連続数
    if l > r: return False
    T = "a" * (r - l) + S
    return T == T[::-1]


print("Yes" if judge() else "No")
