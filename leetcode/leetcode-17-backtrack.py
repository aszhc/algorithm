# encoding=utf8
"""

"""


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        number = {
            '2': list('abc'),
            '3': list('def'),
            '4': list('ghi'),
            '5': list('jkl'),
            '6': list('mno'),
            '7': list('pqrs'),
            '8': list('tuv'),
            '9': list('wxyz'),
            }
        if not digits:
            return []
        lC1 = ['']
        for i in digits:
            ls1 = [x + y for x in lC1 for y in number[i]]
        return ls1

if __name__ == "__main__":
    Sol = Solution()
    end = Sol.letterCombinations("23")
    print(end)


