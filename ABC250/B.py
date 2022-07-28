N, A, B = map(int, input().split())
grid = []

for _ in range(5):
    for _ in range(A):
        grid.append(("." * B + "#" * B) * 5)
    for _ in range(A):
        grid.append(("#" * B + "." * B) * 5)

for row in range(A * N):
    print(grid[row][:B * N])
