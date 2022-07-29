S = input()

j1 = not S.islower()
j2 = not S.isupper()
j3 = len(S) == len(set(S))

judge = j1 and j2 and j3
print("Yes" if judge else "No")
