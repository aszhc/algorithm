package main

import "fmt"

// 暴力法
/*
func maxSlidingWindow(nums []int, k int) []int {
	var result []int

	for i, j := 0, k-1; j >= 0 && j < len(nums); j++ {
		max := nums[i]
		for k := j; k > i; k-- {
			if max < nums[k] {
				max = nums[k]
			}
		}
		result = append(result, max)
		i++
	}
	return result
}
*/

// 滑动窗口
/*
初始化一个双端队列，保持队列头部一直为最大值，
新进来的值将队列尾部小的值不断的剔除出去
，当遍历量大于K时，判断队列头部的值还能不能存在，不能就将上一个K区间最大值剔除
*/

func maxSlidingWindow(nums []int, k int) []int {
	ret := make([]int, 0)
	stack := make([]int, 0)
	for i := 0; i < len(nums); i++ {
		if i >= k && nums[i-k] == stack[0] {
			stack = stack[1:]
		}
		for len(stack) != 0 && stack[len(stack)-1] < nums[i] {
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, nums[i])
		if i >= k-1 {
			ret = append(ret, stack[0])
		}
	}
	return ret

}

func main() {
	nums := []int{1, 3, -1, -3, 5, 3, 6, 7}
	k := 3
	ans := maxSlidingWindow(nums, k)
	fmt.Println(ans)
}
