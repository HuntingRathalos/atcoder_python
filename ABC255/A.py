r, c = map(int, input().split())

list = [list(map(int, input().split())) for _ in range(2)]

print(list[r-1][c-1])
# zipは複数のイテラブルオブジェクトの要素を盾に持ってくるイメージ
# 二次元配列（複数列）の向きを変えたいとき
