def main():
    def solve(x):
        r = N
        for t in range(10 ** 8):
            if Count[x][t % 10] > 0:
                Count[x][t % 10] -= 1
                r -= 1
            if r == 0:
                return t
    N = int(input())
    S = [input() for _ in range(N)]
    Count = [[0] * 10 for _ in range(10)]
    for i in range(N):
        for j in range(10):
            Count[int(S[i][j])][j] += 1
    Time =  [solve(i) for i in range(10)]
    print(min(*Time))
main()
