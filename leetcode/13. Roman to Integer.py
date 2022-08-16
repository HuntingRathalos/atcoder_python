class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        n = len(s)
        ans = 0
        for i in range(n):
            if  i==n-1 or romans[s[i]] >= romans[s[i+1]] :
                ans += romans[s[i]]
            else :
                ans -= romans[s[i]]

        return ans
