class Solution:
    def longestCommonPrefix(self, strs) -> str:
        ans = ""
        for letter_group in zip(*strs):
            if len(set(letter_group)) == 1:
                ans += letter_group[0]
            else:
                return ans
        return ans
