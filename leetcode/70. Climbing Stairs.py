class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [1] * (n + 1)
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


# class Fib_memo:
#     def __init__(self) -> None:
#         self.memo = {0: 1,1: 1}
#     def fib(self, n):
#         if n == 0 or n == 1:
#             return 1
#         if n in self.memo.keys():
#             return self.memo[n]
#         self.memo[n] = self.fib(n - 1) + self.fib(n - 2)
#         return self.memo[n]
