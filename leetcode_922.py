# encoding=utf8
""" 
给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。

对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。

你可以返回任何满足上述条件的数组作为答案。

 

示例：

输入：[4,2,5,7]
输出：[4,5,2,7]
解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
 

提示：

2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-array-by-parity-ii


反思: 此题复习了zip函数的使用(将两个列表生成一个zip对象,然后迭代生成一个新的数组))

"""
class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        right = [i for i in A if i % 2]  # 不能被2整除 
        left = [i for i in A if not i % 2]  # 能被2整除
        zip1 = zip(left,right)
        ans = []
        for i in zip1:
            for j in i:
                ans.append(j)
        return ans


    
if __name__ == "__main__":
    S = Solution()
    ans = S.sortArrayByParityII([4,2,5,7])
    print(ans)
    # S.sortArrayByParityII([1,2,5,8])