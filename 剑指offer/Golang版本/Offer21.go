package main

import "fmt"

/*
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

示例：

输入：nums =[1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof
*/
func exchange(nums []int) []int {
	left, right := 0, len(nums) - 1
	for left < right{
		for left < right && nums[left]%2==1{
			left ++
		}
		for left < right && nums[right]%2==0{
			right --
		}
		nums[left], nums[right] = nums[right], nums[left]
	}
	return nums
}

func main() {
	nums := []int{1, 2, 3, 4, 5}
	ans := exchange(nums)
	fmt.Println(ans)
}
