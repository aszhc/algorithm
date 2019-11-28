# -*- coding: utf-8 -*-
""" 
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1:

输入: "hello"
输出: "holle"
示例 2:

输入: "leetcode"
输出: "leotcede"
说明:
元音字母不包含字母"y"。

在真实的面试中遇到过这道题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-vowels-of-a-string

"""
class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        word = 'aeiouAEIOU'
        filter_word = [i for i in s if i in word]
        ret = list(s)
        for idx, val in enumerate(ret):
            if val in word:
                ret[idx] = filter_word.pop()
        
        return ''.join(ret)
        

if __name__ == "__main__":
    s = Solution()

    a = s.reverseVowels('f*sbl(kjad)(@#vbgyy')
    print(a)

