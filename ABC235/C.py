from sys import stdin
from collections import defaultdict
def solve():
    N, Q = map(int, stdin.readline().split())
    A = list(map(int, stdin.readline().split()))
    D = defaultdict(list)
    for i, a in enumerate(A):
        D[a].append(i + 1)
    for _ in range(Q):
        x, k = map(int, stdin.readline().split())
        if k <= len(D[x]):
            print(D[x][k - 1])
        else:
            print(-1)
solve()
