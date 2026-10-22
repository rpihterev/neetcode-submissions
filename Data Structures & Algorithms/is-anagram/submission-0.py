class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t:
            return True
        if len(s) != len(t):
            return False
        seen1 = {}
        for char in s:
            if char not in seen1:
                seen1[char] = 1
            else:
                seen1[char] += 1
        seen2 = {}
        for char in t:
            if char not in seen2:
                seen2[char] = 1
            else:
                seen2[char] += 1
        
        for key in seen1:
            if key in seen2:
                if seen1[key] != seen2[key]:
                    return False
            else:
                return False
        return True
        

        