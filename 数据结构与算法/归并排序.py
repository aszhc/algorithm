# encoding=utf8
def MergerSort(lists):
    if len(lists) <= 1:
        return lists
    num = len(lists)//2
    # 递归拆分
    left = MergerSort(lists[:num])
    right = MergerSort(lists[num:])
    # print("left", left, "right", right)
    # 合并
    return Merge(left, right)


def Merge(left, right):
    """合并"""
    r, l = 0, 0
    result = []
    # 将两个指针分别指向左和右的一端
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    # 将剩余的再加到结果中
    result += left[l:] + right[r:]
    return result


# print(MergerSort([22,3,2,8,65,8,9,1,4,3]))
print(MergerSort([8, 6, 2, 1, 9]))
# print(MergerSort([1,2,3,4,5,6,7,0]))