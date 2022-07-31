from sys import stdin

N, M = map(int, stdin.readline().split())

UV = [list(map(int, stdin.readline().split())) for _ in range(M)]

ans = 0

l = []
for a in range(1, N + 1):
  for b in range(1, N + 1):
    for c in range(1, N + 1):
      if a != b and b != c and c != a:
        l.append([a, b, c])

for v in l:
  if [v[0], v[1]] in UV and [v[1], v[2]] in UV and [v[0], v[2]] in UV:
    ans += 1


print(ans)
