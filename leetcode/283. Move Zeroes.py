class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_length = len(nums)
        i, j = 0, 0
        while(i < nums_length):
            if nums[j] == 0:
                nums.pop(j)
                nums.append(0)
                i += 1
                continue
            j += 1
            i += 1

        # i = 0
        # j = i + 1

        # while j < len(nums):
        #     if nums[i] == 0 and nums[j] == 0:
        #         j += 1
        #     elif nums[i] == 0 and nums[j] != 0:
        #         nums[i], nums[j] = nums[j], nums[i]
        #         i += 1
        #         j += 1
        #     elif nums[i] != 0 and nums[j] == 0:
        #         i += 1
        #         j += 1
        #     elif nums[i] != 0 and nums[j] != 0:
        #         i += 1
        #         j += 1

        # count=nums.count(0)

        # for i in range(0,count):
        #     nums.remove(0)
        #     nums.append(0)
