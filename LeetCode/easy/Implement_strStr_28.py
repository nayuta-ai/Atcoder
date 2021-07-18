class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        num=len(needle)
        for i in range(len(haystack)):
            if str(haystack[i:i+num])==str(needle[:num]):
                return i
        if not needle:
            return 0
        else:
            return -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)