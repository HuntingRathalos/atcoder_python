N, P = map(int, input().split())
A = list(map(int, input().split()))
ans = 0

for x in A:
    if x < P:
        ans += 1
print(ans)
