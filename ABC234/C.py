K = int(input())
# format 単語に適用するときformat(n, 形式) 文の一部に埋め込む時 "aaa{}aa".format()のようなイメージ
b = format(K, 'b')  # bの型はstrです
ans = b.replace('1', '2') # str型であるbの'1'を'2'に置き換えます
print(ans)
