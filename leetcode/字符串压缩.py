#!/usr/bin/python3

class Solution:
    def compressString(self, S: str) -> str:
        if not S:
            return ''
        cnt = 0
        ch = S[0]
        ans = ''
        for i in S:
            if ch == i:
                cnt +=1
            else:
                ans += ch + str(cnt)
                ch = i
                cnt = 1
        ans += ch + str(cnt)

        return ans if len(ans) <= len(S) else S


if __name__ == "__main__":
    S = "aabcccccaa"
    Sol = Solution()
    ans = Sol.compressString(S)
    print(ans)
