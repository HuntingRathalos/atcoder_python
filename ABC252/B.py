N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

max_A = max(A)
for i in B:
  if A[i - 1] == max_A:
    print('Yes')
    exit()
print('No')
