from sys import stdin
def main():
    N = int(stdin.readline())
    seen = set()
    max_t = -1
    ans = 0
    for i in range(1, N + 1):
        s, t = stdin.readline().split()
        int_t = int(t)
        if s in seen:
            continue
        seen.add(s)
        if max_t < int_t:
            max_t = int_t
            ans = i
    return ans
print(main())


