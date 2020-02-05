class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # if not candidates:
        #     return []
        # n = len(candidates)
        # res = []
        # candidates.sort()
        #
        # def helper(i, tmp, target):
        #     if target == 0:
        #         res.append(tmp)
        #         return
        #     if i == n or target < candidates[i]:
        #         return
        #     helper(i, tmp + [candidates[i]], target - candidates[i])
        #     helper(i+1, tmp, target)
        # helper(0, [], target)
        # return res
        candidates.sort()
        n = len(candidates)
        res = []

        def backtrack(i, tmp_sum, tmp):
            if tmp_sum > target or i == n:
                return
            if tmp_sum == target:
                res.append(tmp)
                return
            for j in range(i, n):
                if tmp_sum + candidates[j] > target:
                    break
                backtrack(j, tmp_sum + candidates[j], tmp + [candidates[j]])

        backtrack(0, 0, [])
        return res


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    Sol = Solution()
    end = Sol.combinationSum(candidates, target)
    print(end)
