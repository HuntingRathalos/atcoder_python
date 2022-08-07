from sys import stdin
from collections import defaultdict

def solve():
    N = int(stdin.readline())
    XY = [list(map(int, stdin.readline().split())) for _ in range(N)]
    S = stdin.readline()
    L_max = defaultdict(lambda: -10**15)
    R_min = defaultdict(lambda: 10**15)
    for s, xy in zip(S, XY):
        if s == "L":
            L_max[xy[1]] = max(L_max[xy[1]], xy[0])
        else:
            R_min[xy[1]] = min(R_min[xy[1]], xy[0])
    for y in L_max.keys():
        if R_min[y] < L_max[y]:
            return True
    return False

print("Yes" if solve() else "No")

