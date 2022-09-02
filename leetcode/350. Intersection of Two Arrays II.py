class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import defaultdict
        d = defaultdict(int)
        result = []
        for num in nums1:
            d[num] += 1
        for num in nums2:
            if (num in d) and d[num] > 0:
                result.append(num)
                d[num] -= 1
        return result
