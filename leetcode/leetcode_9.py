class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False

    
if __name__ == "__main__":
    s = Solution()
    T = s.isPalindrome
