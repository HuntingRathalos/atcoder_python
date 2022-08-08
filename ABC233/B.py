from operator import iadd
from re import I


def solve():
    ans = 0
    # 2点の組み合わせ（完全に２重ループする必要なし）
    for i in range(N):
        x1, y1 = XY[i]
        # このiをNにする必要がない
        for j in range(i):
            if i == 0:
                continue
            x2, y2 = XY[j]
            l = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            ans = max(ans, l)
    return ans


N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
print(solve())
