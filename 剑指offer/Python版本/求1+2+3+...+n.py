"""
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

"""


class Solution:
    def Sum_Solution(self, n):
        # write code here
        return n and n + self.Sum_Solution(n - 1)


if __name__ == '__main__':
    Sol = Solution()
    ans = Sol.Sum_Solution(0)
    print(ans)
