N = int(input())
T = list(input())
d = [[1, 0], [0, -1], [-1, 0], [0, 1]]
direction = 0
xy = [0, 0]
for i in T:
    if i == "S":
        xy[0] += d[direction][0]
        xy[1] += d[direction][1]
    else:
        direction += 1
        direction %= 4
print(*xy)
