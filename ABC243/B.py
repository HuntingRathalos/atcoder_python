def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    one = 0
    two = 0

    for i in range(N):
        if A[i] == B[i]:
            one += 1
        else:
            if A[i] in B:
                two += 1
    print(one, two, sep='\n')

solve()

