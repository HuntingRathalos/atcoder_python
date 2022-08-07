def solve():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))

    ans = sum(A)
    rem = K
    Q = sum(x // X for x in A)
    R = sorted((x % X for x in A), reverse=True)
    ans -= X * min(Q, rem)
    rem -= min(Q, rem)
    for i in range(N):
        if rem >= 1:
            rem -= 1
            ans -= R[i]
        else:
            break
    # ans -= sum(R[:rem])  # 大きい順に使う（スライスは配列外参照を起こさない）
    return ans
print(solve())
