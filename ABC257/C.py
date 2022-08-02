from bisect import bisect_left

N = int(input())
S = input()
W = list(map(int, input().split()))

a = [W[i] for i in range(N) if S[i] == '0']
a.sort()
b = [W[i] for i in range(N) if S[i] == '1']
b.sort()
c = []
for x in W:
    c.append(x)
    c.append(x + 0.1)

result = 0
for x in c:
    result = max(result, bisect_left(a, x) + len(b) - bisect_left(b, x))
print(result)
