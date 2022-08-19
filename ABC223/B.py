def calc():
    for row1 in range(H):
        for row2 in range(row1 + 1, H):
            for col1 in range(W):
                for col2 in range(col1 + 1, W):
                    if A[row1][col1] + A[row2][col2] > A[row2][col1] + A[row1][col2]:
                        return False
    return True


H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

print("Yes" if calc() else "No")
