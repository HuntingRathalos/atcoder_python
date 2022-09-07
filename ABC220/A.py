A, B, C = map(int, input().split())
# 『B 以下で最大の C の倍数』は ⌊BC⌋×C⌊BC⌋×C で求められます
# （B を C で割って切り捨てて CC を掛ける）
x = B // C * C
print(x if x >= A else -1)

# for i in range(A, B + 1):
#     if i % C == 0:
#         print(i)
# print(-1)
