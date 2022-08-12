N, X = map(int, input().split())
A = [0] + list(map(int, input().split()))  # A[1]が友達1の情報を表すようにしたいので、A[0]にダミーを入れてずらします
flag = [False] * (N + 1)  # flag[i] が True なら、友達iは秘密を知っています
flag[X] = True
now = X  # はじめに秘密を知ったのは友達Xです
while not flag[A[now]]:  # 友達A_iがまだ秘密を知らなければ、A_iに伝えます（知っていればそこで終了です）
    now = A[now]
    flag[now] = True
print(flag.count(True))
