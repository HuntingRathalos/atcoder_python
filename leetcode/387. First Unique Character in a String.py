class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import defaultdict
        d = defaultdict(int)
        for i in s:
            d[i] += 1
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1
