class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left = left + 1
            right = right - 1
        return s
        # s.reverse()


if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    Sol = Solution()
    end = Sol.reverseString(s)
    print(end)
