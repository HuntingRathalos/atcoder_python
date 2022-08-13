from bisect import bisect_left

def solve():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for _ in range(Q):
        x = int(input())
        less_than_x_count = bisect_left(A, x)
        print(N - less_than_x_count)

solve()
