class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import defaultdict
        d = defaultdict(int)
        for num in nums:
            if d[num] + 1 > (len(nums) // 2):
                return num
            else:
                d[num] += 1
