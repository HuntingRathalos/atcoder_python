class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        from collections import defaultdict
        s_counter = defaultdict(int)
        t_counter = defaultdict(int)
        for s_char, t_char in zip(s, t):
            s_counter[s_char] += 1
            t_counter[t_char] += 1

        return s_counter == t_counter

