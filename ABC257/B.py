N,K,Q=map(int,input().split())
A=list(map(int,input().split()))
L=list(map(int,input().split()))

S=[0]*(N+1)
for i in range(K):
  S[A[i]] = 1

for i in range(Q):
    Count=0

    for Now in range(1,N):
        if S[Now]==1:
            Count+=1
            if Count==L[i]:
                if S[Now+1]==0:
                    S[Now+1]=1
                    S[Now]=0
                    break
ans=[]

for i in range(1,N+1):
    if S[i]==1:
        ans.append(i)

print(*ans)

