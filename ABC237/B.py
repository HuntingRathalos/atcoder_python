H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

ans = list(zip(*A))

for i in ans:
    print(*i)
