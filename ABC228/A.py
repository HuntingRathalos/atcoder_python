S, T, X = map(int, input().split())

if S < T:  # 日付が変わらない場合
    print("Yes" if S <= X < T else "No")  # T時30分に電気は消えていますから、Tは含みません
else:  # 日付が変わる場合
    print("Yes" if 0 <= X < T or S <= X < 24 else "No")
