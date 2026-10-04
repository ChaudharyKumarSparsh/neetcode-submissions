class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # flg = -1
        
        dict1 = {}
        dict2 = {}
        for i in range(len(s)):
            dict1[s[i]] = dict1.get(s[i], 0) + 1
        for i in range(len(t)):
            dict2[t[i]] = dict2.get(t[i], 0) + 1
        for i in dict1:
            if dict1[i] != dict2.get(i):
                return False
        for i in dict2:
            if dict2[i] != dict1.get(i):
                return False
        return True
        # return True