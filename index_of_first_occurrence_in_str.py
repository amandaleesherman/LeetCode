class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack.count(needle) > 0:
            return haystack.find(needle) #rets index of first occurrence of char in str
        return -1 
    #beats 85% of solns, 100% accuracy
    