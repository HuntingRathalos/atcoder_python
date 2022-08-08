def solve():
    S = input()
    T = input()
    A = [ord(char) - ord('a') for char in S]
    B = [ord(char) - ord('a') for char in T]
    for k in range(26):
        C = [(x + k) % 26 for x in A]
        if B == C:
            return True
    return False


print("Yes" if solve() else "No")
