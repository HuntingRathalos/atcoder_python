N = int(input())
A = list(map(int, input().split()))

for k in range(1, N):
    # A[0]...A[k-1] に A[k] を挿入する
    # A[k] を挿入する位置を、実際に移動させながら求める
    while k and A[k-1]>A[k]:
        A[k-1], A[k] = A[k], A[k-1]
        k -= 1

    print(*A)
