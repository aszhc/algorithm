#!/usr/bin/python3


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.grid = grid
        self.m = len(grid)  # 行
        self.n = len(grid[0])  # 列
        res = 0

        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 1:
                    res = max(res, self._dfs(i, j))
        return res

    def _dfs(self, i, j):
        if self._check_no_valid(i, j) or self.grid[i][j] != 1:
            return 0
        self.grid[i][j] = -1  # -1表示遍历过这个点了
        return 1 + self._dfs(i-1, j) + self._dfs(i, j+1) + self._dfs(i+1, j) + self._dfs(i, j-1)

    def _check_no_valid(self, i, j):
        return i < 0 or i >= self.m or j < 0 or j >= self.n


if __name__ == "__main__":
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

    Sol = Solution()
    ans = Sol.maxAreaOfIsland(grid)
    print(ans)
