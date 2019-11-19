# encoding=utf8
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        ss  = list(map(set,zip(*strs)))
        print(ss)
        res = ""
        for i ,x in enumerate(ss):
            pass

if __name__ == "__main__":
    Sol = Solution()
    Sol.longestCommonPrefix(["flower","flow","flight"])



