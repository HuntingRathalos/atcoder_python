from collections import defaultdict

def solve():
    def calc(Chosed):
        D = defaultdict(int)
        for i in Chosed:
            for chr in S_list[i]:
                D[chr] += 1
        score = 0
        for chr, count in D.items():
            if count == K:
                score += 1
        return score

    N,K=map(int,input().split())
    S_list = [input() for _ in range(N)]
    ans = 0
    for bit in range(1<<N):
        Chosed = []
        for shift in range(N):
            if bit >> shift & 1:
                Chosed.append(shift)
        ans = max(ans, calc(Chosed))
    return ans
print(solve())


