from collections import defaultdict
def solve():
    N, M = map(int, input().split())
    D = defaultdict(int)
    S = input().split()
    T = input().split()
    for t in T:
        D[t] += 1
    for s in S:
        if D[s] == 1:
            print("Yes")
        else:
            print("No")
solve()
