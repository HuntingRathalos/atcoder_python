from sys import stdin

def solve():
    def judge(list):
        return len(list) == N - 1

    N = int(stdin.readline())
    S = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, stdin.readline().split())
        S[a].append(b)
        S[b].append(a)
    for i in range(1, N + 1):
        if judge(S[i]):
            return "Yes"
    return "No"
print(solve())
