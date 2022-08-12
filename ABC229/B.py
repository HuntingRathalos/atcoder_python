def solve():
    A, B = input().split()
    X, Y = A.zfill(19), B.zfill(19)  # 0000...229のような、左から0埋めされた長さ20の文字列ができます
    for x, y in zip(X, Y):
        if int(x) + int(y) >= 10:
            return "Hard"
    return "Easy"


print(solve())
