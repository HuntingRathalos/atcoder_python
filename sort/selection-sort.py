N = int(input())
A = list(map(int, input().split()))

for k in range(N-1):
    # 未ソートの要素のうち最小値がある位置を求める
    min_element_index = A[k:].index(min(A[k:])) + k

    # 未ソートの要素の先頭 A[k] と最小値を入れ替え、
    # 次のループでは A[0]...A[k] をソート済みとみなす
    A[k], A[min_element_index] = A[min_element_index], A[k]

    # 現時点での配列の中身を出力する
    print(*A)
