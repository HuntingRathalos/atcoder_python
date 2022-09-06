def judge():
        if S == T:
                return True
        for i in range(len(S) - 1):
                L = list(S)
                L[i], L[i + 1] = L[i + 1], L[i]
                S2 = ''.join(L)
                if S2 == T:
                        return True
        return False
S = input()
T = input()
print('Yes' if judge() else 'No')
