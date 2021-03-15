package main

import (
	"fmt"
)

/*
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]
示例 2：

输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof
*/

func twoSum(nums []int, target int) []int {
	//left, right := 0, len(nums)-1
	//for left < right {
	//	sum := nums[left] + nums[right]
	//	if sum > target {
	//		right--
	//	} else if sum < target {
	//		left++
	//	} else {
	//		return []int{nums[left], nums[right]}
	//	}
	//}
	//return nil
	m := make(map[int]struct{})
	for _, v := range nums {
		if _, ok := m[target]; ok {
			return []int{target - v, v}
		} else {
			m[v] = struct{}{}
		}
	}
	return nil
}

func main() {
	nums := []int{16, 16, 18, 24, 30, 32}
	target := 48
	ans := twoSum(nums, target)
	fmt.Println(ans)
}
