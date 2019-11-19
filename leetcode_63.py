#encoding=utf8
"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths-ii
示例 1:

输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths-ii
"""

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if(not obstacleGrid):
            return 0
        if(obstacleGrid[0][0]==1 or obstacleGrid[-1][-1]==1):
            return 0
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[0]*n for _ in range(m)]
        dp[0][0]=1
        for i in range(1,n):
            if(obstacleGrid[0][i]!=1):
                dp[0][i]=dp[0][i-1]
        for j in range(1,m):
            if(obstacleGrid[j][0]!=1):
                dp[j][0]=dp[j-1][0]
        for x in range(1,m):
            for y in range(1,n):
                if(obstacleGrid[x][y]!=1):
                    dp[x][y]=dp[x-1][y]+dp[x][y-1]
        return dp[-1][-1]



if __name__ == "__main__":
    ques = [[0,0,0],[0,1,0],[0,0,0]]
    Sol = Solution()
    end = Sol.uniquePathsWithObstacles(ques)
    print(end)
