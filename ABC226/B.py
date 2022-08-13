def calc(a, b):
    return 4 * a * b + 3 * a + 3 * b

N = int(input())
S = list(map(int, input().split()))
T = set()
# f(a,b)=4ab+3a+3b（最大値1000）より、aに1を代入するとbの最大は142となる。（bも同様）
for a in range(1, 143):
    for b in range(1, 143):
        T.add(calc(a, b))

ans = 0

for x in S:
    if x not in T:
        ans += 1

print(ans)
