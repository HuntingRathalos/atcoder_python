N = int(input())
A = list(map(int,input().split()))

P = 0
koma = [0]

for i in range(N):
  new_coma = [0]

  for j in koma:
    if j + A[i] < 4:
      new_coma.append(j + A[i])
    else:
      P += 1
  koma = new_coma

print(P)
