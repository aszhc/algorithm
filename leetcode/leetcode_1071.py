#!/usr/bin/python3
import math


class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # candidate_len = math.gcd(len(str1), len(str2))
        # candidate = str1[: candidate_len]
        # if str1 + str2 == str2 + str1:
        #     return candidate
        # return ''
        if str1 + str2 != str2 + str1:
            return ''
        different = len(str1) - len(str2)
        if different == 0:
            return str1
        elif different > 0:
            str1 = str1[len(str2):len(str1)]
        else:
            str2 = str2[len(str1):len(str2)]
        return self.gcdOfStrings(str1, str2)


if __name__ == "__main__":
    str1 = "ABCABC"
    str2 = "ABC"
    Sol = Solution()
    ans = Sol.gcdOfStrings(str1, str2)
    print(ans)
