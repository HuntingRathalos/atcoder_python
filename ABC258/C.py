from sys import stdin

N, Q = map(int, stdin.readline().split())
S = stdin.readline().rstrip()

start = 0
result = []

for _ in range(Q):
    t, x = map(int, stdin.readline().split())
    if t == 1:
        start = (start - x) % len(S)
    elif t == 2:
        result.append(S[(start + x - 1) % len(S)])
print(*result, sep="\n")
