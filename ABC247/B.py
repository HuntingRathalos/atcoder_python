N = int(input())
ST = [input().split() for _ in range(N)]

for i in range(N):
    can_give = False
    for S in ST[i]:
        ok = True
        for j in range(N):
            if i != j:
                if S == ST[j][0] or S == ST[j][1]:
                    ok = False
        if ok == True:
            can_give = True
    if can_give == False:
        print("No")
        exit()
print("Yes")


