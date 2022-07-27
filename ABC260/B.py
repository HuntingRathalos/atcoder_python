N,X,Y,Z=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

ans = []

math = []

for i in range(N):
  math.append([A[i], -(i + 1)])
math.sort(reverse=True)

for i in range(X):
  ans.append(-math[i][1])

eng = []

for i in range(N):
  if (i + 1) not in ans:
    eng.append([B[i], -(i + 1)])
eng.sort(reverse=True)

for i in range(Y):
  ans.append(-eng[i][1])

sum = []

for i in range(N):
  if (i + 1) not in ans:
    sum.append([A[i] + B[i], -(i + 1)])
sum.sort(reverse=True)

for i in range(Z):
  ans.append(-sum[i][1])

ans.sort()
for i in ans:
  print(i)
