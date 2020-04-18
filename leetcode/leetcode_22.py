#!/usr/bin/python3

class Solution:
    def generateParenthesis(self, n: int):
        ans = []
        def backtrack(S = '',left=0,right=0):
            if left == n and right ==n:
                ans.append(S)
                return
            if left < n:
                backtrack(S+'(',left+1,right)
            if right <left and right < n:
                backtrack(S+')',left,right+1)

        backtrack()
        return ans


if __name__ == "__main__":
    Sol = Solution()
    ans = Sol.generateParenthesis(3)
    print(ans)