class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"(": ")", "[": "]", "{": "}"}
        list = []
        for char in s:
            if char in dic:
                list.append(char)
            else:
                if (len(list) and dic[list[-1]] == char):
                    list.pop(-1)
                else:
                    return False
        return list == []
