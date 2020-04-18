#!/usr/bin/python3


class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        target = sum(A)
        if target % 3 != 0:
            return False
        count = add = 0
        for i in A:
            add += i
            if add == target//3:
                count += 1
                add = 0
        return count >= 3


if __name__ == "__main__":
    # A = [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]
    A = [0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]
    # A = [3, 3, 6, 5, -2, 2, 5, 1, -9, 4]
    # A = [10,-10,10,-10,10,-10,10,-10]

    Sol = Solution()
    ans = Sol.canThreePartsEqualSum(A)
    print(ans)
