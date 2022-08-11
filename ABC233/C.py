def solve():
    N, X = map(int, input().split())
    nums = [1]
    for i in range(N):
        L, *A = map(int, input().split())
        tmp_nums = []
        for a in A:
            for num in nums:
                tmp_nums.append(a * num)
        nums = tmp_nums
    return nums.count(X)
print(solve())
