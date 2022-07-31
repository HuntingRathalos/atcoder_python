Y = int(input())

r = Y % 4

if r == 0:
    print(Y + 2)
if r == 1:
    print(Y + 1)
if r == 2:
    print(Y)
if r == 3:
    print(Y + 3)
