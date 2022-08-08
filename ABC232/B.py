L, R = map(int, input().split())
L = L - 1  # Lを0はじまりにします（Rはスライスの終端になりますが、R自体は含まないのでそのままでいいです）
S = input()
S_list = list(S)  # 文字列はイミュータブル（変更不可）なので、一度文字列のリストにします
S_list[L:R] = S_list[L:R][::-1]  # [::-1] で反転したものを代入します
print(*S_list, sep='')
