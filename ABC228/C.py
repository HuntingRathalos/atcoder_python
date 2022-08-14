N, K = map(int, input().split())
S = [sum(map(int, input().split())) for _ in range(N)]
S_sorted = [10000] + sorted(S, reverse=True)  # S_sorted[K]が暫定K位を表すよう、0番目にダミーを入れる
border = S_sorted[K]  # 暫定K位の点数
for score in S:
    print("Yes" if score + 300 >= border else "No")  # 同点でもOK
