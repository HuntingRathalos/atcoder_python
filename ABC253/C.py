from sys import stdin
from collections import defaultdict
import heapq
def solve():
    Q = int(stdin.readline())
    Count = defaultdict(int)
    MaxQue=[]
    MinQue=[]

    for _ in range(Q):
        query = list(map(int, stdin.readline().split()))
        if query[0] == 1:
            x = query[1]
            Count[x] += 1
            heapq.heappush(MinQue, x)
            heapq.heappush(MaxQue, -x)
        elif query[0] == 2:
            x=query[1]
            c=query[2]
            Count[x] -= min(c, Count[x])
        elif query[0] == 3:
            S_min = heapq.heappop(MinQue)
            while Count[S_min] == 0:
                S_min = heapq.heappop(MinQue)
            S_max = heapq.heappop(MaxQue) * -1
            while Count[S_max] == 0:
                S_max = heapq.heappop(MaxQue) * -1
            print(S_max - S_min)

            heapq.heappush(MinQue, S_min)
            heapq.heappush(MaxQue, -S_max)

solve()
