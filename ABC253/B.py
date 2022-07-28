H,W = map(int, input().split())
S = [list(input()) for _ in range(H)]
P = []
for h in range(H):
    for w in range(W):
        if S[h][w] == 'o':
            P.append([h, w])
x1, y1 = P[0]
x2, y2 = P[1]

ans = abs(x1 - x2) + abs(y1 - y2)
print(ans)
