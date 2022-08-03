from sys import stdin
def main():
    N, Q = map(int, stdin.readline().split())
    A = list(range(N +  1))
    A_idx = list(range(N +  1))
    for _ in range(Q):
        x = int(stdin.readline())
        bi = A_idx[x]
        ai = bi + 1 if bi != N else  bi - 1
        y = A[ai]
        A[bi], A[ai] = A[ai], A[bi]
        A_idx[x], A_idx[y] = A_idx[y], A_idx[x]
    print(*A[1:])
main()

