# encoding=utf-8
""" 
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters

** 滑动窗口 **

"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_count = 0
        count = 0
        words = ''
        for i in s:
            if i not in words:
                words += i
                count += 1
            else:
                if count > max_count:
                    max_count = count
                index = words.index(i)
                words = words[(index+1):] + i
                count = len(words)
        if count > max_count:
            max_count = count
        return max_count

if __name__ == "__main__":
    S = Solution()
    ans = S.lengthOfLongestSubstring("pwwkew")
    print(ans)
