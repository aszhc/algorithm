#!/usr/bin/python3
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        Rows = len(grid)
        Columns = len(grid[0])
        queue = []

        count = 0  # 新鲜橘子的数量
        for r in range(Rows):
            for c in range(Columns):
                if grid[r][c] == 1:
                    count += 1
                elif grid[r][c] == 2:
                    queue.append([r, c])
        round = 0  # 表示分钟数
        while count > 0 and len(queue) > 0:
            round += 1
            n = len(queue)
            # while queue:
            for i in range(n):
                r, c = queue.pop(0)
                if r-1 >= 0 and grid[r-1][c] == 1:  # 左
                    grid[r-1][c] = 2
                    count -= 1
                    queue.append([r-1, c])
                if r+1 < Rows and grid[r+1][c] == 1:  # 右
                    grid[r+1][c] = 2
                    count -= 1
                    queue.append([r+1, c])
                if c-1 >= 0 and grid[r][c-1] == 1:  # 上
                    grid[r][c-1] = 2
                    count -= 1
                    queue.append([r, c-1])
                if c+1 < Columns and grid[r][c+1] == 1:  # 下
                    grid[r][c+1] = 2
                    count -= 1
                    queue.append([r, c+1])

        if count > 0:
            return -1
        else:
            return round

    # def orangesRotting(self, grid):
    #     M = len(grid)
    #     N = len(grid[0])
    #     queue = []

    #     count = 0  # count 表示新鲜橘子的数量
    #     for r in range(M):
    #         for c in range(N):
    #             if grid[r][c] == 1:
    #                 count += 1
    #             elif grid[r][c] == 2:
    #                 queue.append((r, c))

    #     round = 0  # round 表示腐烂的轮数，或者分钟数
    #     while count > 0 and len(queue) > 0:
    #         round += 1
    #         n = len(queue)
    #         for i in range(n):
    #             r, c = queue.pop(0)
    #             if r-1 >= 0 and grid[r-1][c] == 1:
    #                 grid[r-1][c] = 2
    #                 count -= 1
    #                 queue.append((r-1, c))
    #             if r+1 < M and grid[r+1][c] == 1:
    #                 grid[r+1][c] = 2
    #                 count -= 1
    #                 queue.append((r+1, c))
    #             if c-1 >= 0 and grid[r][c-1] == 1:
    #                 grid[r][c-1] = 2
    #                 count -= 1
    #                 queue.append((r, c-1))
    #             if c+1 < N and grid[r][c+1] == 1:
    #                 grid[r][c+1] = 2
    #                 count -= 1
    #                 queue.append((r, c+1))

    #     if count > 0:
    #         return -1
    #     else:
    #         return round


if __name__ == "__main__":
    # grid = [[2,1,1],[1,1,0],[0,1,1]]
    # grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    Sol = Solution()
    ans = Sol.orangesRotting(grid)
    print(ans)
