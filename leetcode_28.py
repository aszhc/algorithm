# encoding=utf-8
"""
法1：
if needle in haystack:
            return haystack.index(needle)
        else:
            return -1

"""
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(0,len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)]==needle:
                return i
        return -1

if __name__ == "__main__":
    Sol = Solution()
    end = Sol.strStr("hello","llo")
    print(end)
