s = input()

flag = [True for _ in range(10)]
for i in s:
  flag[int(i)] = False

for k in range(10):
  if flag[k] == True:
    print(k)

