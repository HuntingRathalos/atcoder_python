S = [input() for _ in range(3)]
T = list(map(int, list(input())))
# ans = ''
# for t in T:
#     ans += S[t - 1]
# print(ans)

# 文字列を+=で連結するのは低速で、文字数が多くなるとTLEになる恐れがあり
# リストに文字列をappendして、最後に''.join(L)としてくっつける方法
L = []
for t in T:
    L.append(S[t - 1])
print(''.join(L))
