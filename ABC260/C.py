N, X, Y = map(int, input().split())

# 再帰
# from functools import lru_cache
# @lru_cache(maxsize=None)
# def calc_red(level):
#     if level == 1:
#         return 0
#     return (calc_red(level - 1) + calc_blue(level) * X)

# @lru_cache(maxsize=None)
# def calc_blue(level):
#     if level == 1:
#         return 1
#     return (calc_red(level - 1) + calc_blue(level - 1) * Y)

# print(calc_red(N))

# DP
red = [0] * (N + 1)
blue = [0] * (N + 1)
blue[1] = 1
for i in range(2, N + 1):
    blue[i] = red[i - 1] + blue[i - 1] * Y
    red[i] = red[i - 1] + blue[i] * X
print(red[N])
