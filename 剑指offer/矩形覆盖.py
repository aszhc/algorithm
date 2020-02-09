
"""
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

"""
class Solution:
    def rectCover(self, number):
        if number < 3:
            return number
        a, b = 1, 2
        for i in range(3, number+1):
            a, b = b, a+b
        return b



if __name__ == '__main__':
    Sol = Solution()
    ans = Sol.rectCover(10)
    print(ans)