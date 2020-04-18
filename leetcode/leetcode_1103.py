#!/usr/bin/python3


class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        ans = [0] * num_people
        n = 1
        p = 0
        while candies > n:
            ans[p] += n
            candies -= n
            n += 1
            p += 1
            if p == num_people:
                p = 0
                
        ans[p] += candies
        return ans


if __name__ == "__main__":
    Sol = Solution()
    ans = Sol.distributeCandies(7, 4)
    print(ans)

