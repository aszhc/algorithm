class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        return digits.insert(0, 1)


if __name__ == '__main__':
    digits = [9, 9]
    Sol = Solution()
    end = Sol.plusOne(digits)
    print(end)