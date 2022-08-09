from collections import Counter

N = int(input())
C = Counter()
for _ in range(N):
    s = input()
    C[s] += 1
mc = C.most_common(1)  # [("takahashi", 3)] のような長さ1のリストが得られます
m_tuple = mc[0]  # ("takahashi", 3) を取り出します
m_name, m_count = m_tuple
print(m_name)
