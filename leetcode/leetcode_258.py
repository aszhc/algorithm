#encoding=utf8

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 9:
            return num
        elif num % 9:
            return num % 9
        else:
            return 9

if __name__ == "__main__":
    Sol = Solution()
    end = Sol.addDigits(11)
    print(end)
