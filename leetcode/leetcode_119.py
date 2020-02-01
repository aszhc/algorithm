class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # res = [1]
        # if rowIndex == 0:
        #     return res
        # for i in range(1, rowIndex + 1):
        #     new_row = [a + b for a, b in zip([0] + res, res + [0])]
        #     res = new_row
        # return res

        res = [1]
        for i in range(1, rowIndex + 1):
            res.insert(0, 0)
            for j in range(i):
                res[j] = res[j] + res[j + 1]
        return res


if __name__ == '__main__':
    Sol = Solution()
    end = Sol.getRow(3)
    print(end)
