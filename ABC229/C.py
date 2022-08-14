def solve():
    N, W = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    sort_AB = sorted(AB, key=lambda ab: ab[0], reverse=True)

    ans = 0
    rem = W
    for a, b in sort_AB:
        if rem == 0:
          return ans
        t = min(rem, b)  # bかremの小さい方
        ans += t * a
        rem -= t
    return ans

print(solve())
