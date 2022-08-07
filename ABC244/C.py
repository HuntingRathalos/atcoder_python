def solve():
    N = int(input())
    S = set(range(1, 2 * N + 2))
    while True:
        print(S.pop(), flush=True)
        aoki = int(input())
        if aoki == 0:
            break
        S.remove(aoki)
solve()
