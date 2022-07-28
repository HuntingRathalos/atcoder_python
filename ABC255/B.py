N,K=map(int,input().split())
A=list(map(int,input().split()))

xy = [list(map(int, input().split())) for _ in range(N)]

from math import sqrt
ans = 0
min_dist = []
for x in range(N):
    dist = 10 ** 10
    for y in range(K):
        y = A[y]-1
        dist = min(dist, sqrt((xy[x][0]-xy[y][0])**2+(xy[x][1]-xy[y][1])**2))
    min_dist.append(dist)

print(max(min_dist))
