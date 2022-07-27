n = int(input())
grid = [list(input()) for _ in range(n)]
ans = 0
d = [(1,0), (0,-1), (-1,0), (0,1), (1,1), (1,-1), (-1,-1), (-1,1)]

for x in range(n):
    for y in range(n):
        for dx,dy in d:
            now = grid[x][y]
            now_x = x
            now_y = y
            for z in range(n - 1):
                now_x += dx
                now_y += dy
                now_x %= n
                now_y %= n
                now += grid[now_x][now_y]
            if ans < int(now):
                ans = int(now)
print(ans)
