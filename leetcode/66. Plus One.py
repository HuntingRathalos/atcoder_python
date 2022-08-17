class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_digits = "".join(map(str, digits))
        num = str(int(str_digits) + 1)
        ans = list(map(int, (list(num))))
        return ans
