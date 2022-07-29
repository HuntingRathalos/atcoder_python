N = int(input())
A = list(map(int, input().split()))

D = [0, 360]
degree = 0
for i in range(N):
    degree += A[i]
    degree %= 360
    D.append(degree)
D.sort()

size = [D[i + 1] - D[i] for i in range(len(D) - 1)]

print(max(size))
