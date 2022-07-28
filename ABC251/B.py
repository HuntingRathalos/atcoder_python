N, W = map(int, input().split())
A = list(map(int, input().split())) + [0, 0]

good = [0] * (W + 1)
from itertools import combinations

for x, y, z in combinations(A, 3):
    w = x + y + z
    if w <= W:
        good[w] = 1
print(good.count(1))
