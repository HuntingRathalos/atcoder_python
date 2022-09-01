class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
                return False
        elif n == 1:
                return True
        if n % 3 != 0:
                return False
        else:
                return self.isPowerOfThree(n // 3)


        # while n > 1:
        #         if n % 3 != 0:
        #                 return False
        #         else:
        #                 n //= 3
        # return n == 1

        # 0 % 3で求めているものは3だが,0が返される(うまく動作しない)
        # そのためn != 0が必要
        # while n % 3 == 0 and n != 0:
        #     n //= 3
        # if n == 1: return True
        # return False
