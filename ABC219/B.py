K = int(input())
A, B = input().split()
print(int(A, K) * int(B, K))

# def convert(x, k):
#         ret = 0
#         i = 0
#         while x > 0:
#                 ret += (x % 10) * (k ** i)
#                 x //= 10
#                 i += 1
#         return ret
# ans = convert(A, K) * (B, K)
# print(ans)
