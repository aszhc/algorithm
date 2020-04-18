class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == s[::-1]:
            return s
        max_len = 1
        res = s[0]
        for i in range(len(s) - 1):
            for j in range(i+1, len(s)):
                if j - i + 2 > max_len and s[i:j+1] == s[i:j+1][::-1]:   # j - i + 几 无所谓, 只要大于max_len就行了
                    max_len = j - i + 2
                    res = s[i:j + 1]
        return res


if __name__ == '__main__':
    # s = "babad"
    s = "cbbd"
    Sol = Solution()
    end = Sol.longestPalindrome(s)
    print(end)