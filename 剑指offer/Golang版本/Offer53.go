package main

import "fmt"

func search(nums []int, target int) int {
	if len(nums) == 0 {
		return 0
	}

	left, right, res := 0, len(nums)-1, 0
	for left <= right {
		mid := (left + right) / 2
		if nums[mid] == target {
			break
		} else if nums[mid] < target {
			left = mid + 1
		} else if nums[mid] > target {
			right = mid - 1
		}
	}
	for i := left; i <= right; i++ {
		if nums[i] == target {
			res++
		}
	}

	return res
}

func main() {
	//target := 8
	//nums := []int{5, 7, 7, 8, 8, 10}
	target := 1
	nums := []int{1}
	ans := search(nums, target)
	fmt.Println(ans)
}
