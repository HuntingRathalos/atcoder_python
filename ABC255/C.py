X, A, D, N = map(int, input().split())

def main(X, A, D, N):
    seq_max, seq_min = (A+D*(N-1), A) if D > 0 else (A, A+D*(N-1))

    if X >= seq_max:
        return abs(seq_max - X)
    elif X <= seq_min:
        return abs(seq_min - X)
    else:
        left, right = (0, N-1) if D > 0 else (N-1, 0)
        while abs(left - right) > 1:
            mid = (left + right) // 2
            if A+D*mid > X:
                right = mid
            else:
                left = mid
        return min(abs(A+D*left - X) , abs(A+D*right - X))
print(main(X, A, D, N))
