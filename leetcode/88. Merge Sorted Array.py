class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1[m:] = nums2[:n] これは一応おけ
        # nums1.sort()

        # nums1 = nums1[:m] + nums2[:n] この書き方はダメ
        # nums1.sort()

        temp = nums1[:m]

        for i in range(m + n):
            if len(temp) == 0:
                nums1[i:] = nums2
                break
            elif len(nums2) == 0:
                nums1[i:] = temp
                break
            else:
                if temp[0] < nums2[0]:
                    nums1[i] = temp[0]
                    temp.pop(0)
                    # del temp[0]
                else:
                    nums1[i] = nums2[0]
                    nums2.pop(0)
                    # del nums2[0]
        return nums1
