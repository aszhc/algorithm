# -*- coding:utf-8 -*-
"""
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007
"""


class Solution:
    def InversePairs(self, data):
        # count = 0
        # for i in range(len(data)):
        #     for j in range(i, len(data)):
        #         print(data[i], data[j])
        #         if data[i] > data[j]:
        #             count += 1
        # return count

        # Sortdata = sorted(data)
        # res = 0
        # for i in Sortdata:
        #     res += data.index(i)
        #     data.pop(data.index(i))
        # return res
        count, result = self.merge_sort(data)
        return count % 1000000007

    def merge_sort(self, a_list):
        n = len(a_list)
        count = 0
        if n <= 1:
            return count, a_list
        # 拆分
        count_l, left = self.merge_sort(a_list[:n // 2])
        count_r, right = self.merge_sort(a_list[n // 2:])
        # 合并排序
        count_merge, merge = self.merge(left, right)
        count = count_l + count_r + count_merge
        return count, merge

    def merge(self, left, right):
        count = 0
        l = r = 0
        result = []
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
                # 当右边的元素被插入时，证明这个元素比左边的剩下的所有元素都小
                # 可以组成len(left)-l个逆序对
                count += len(left) - l
        result += left[l:] + right[r:]
        return count, result


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 0]
    Sol = Solution()
    ans = Sol.InversePairs(data)
    print(ans)
