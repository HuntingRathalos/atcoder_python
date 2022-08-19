S = input()
n = len(S)
L = []

for _ in range(n):
    L.append(S)
    S = S[1:] + S[0]
L.sort()

print(L[0])
print(L[-1])
