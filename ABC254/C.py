from operator import mod


def solve():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    mod_group = [[] for _ in range(K)]

    for i in range(N):
        mod_group[i % K].append(a[i])
    for j in range(K):
        mod_group[j].sort()

    b = []
    for i in range(N):
        b.append(mod_group[i % K][i // K])
    return sorted(a) == b
print("Yes" if solve() else "No")
