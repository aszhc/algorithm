// package main

// import "fmt"

// func quickSort(nums []int) []int {
// 	sort(nums, 0, len(nums)-1)
// 	return nums
// }

// func sort(nums []int, low, high int) {
// 	if low < high {
// 		mid := partition(nums, low, high)
// 		sort(nums, low, mid-1)
// 		sort(nums, mid+1, high)
// 	}
// }

// func partition(nums []int, low, high int) int {
// 	pivot := nums[high]
// 	i := low - 1
// 	for j := low; j < high; j++ {
// 		if nums[j] < pivot {
// 			i++
// 			nums[j], nums[i] = nums[i], nums[j]
// 		}
// 	}
// 	nums[i+1], nums[high] = nums[high], nums[i+1]
// 	return i + 1
// }

// // 二分查找
// func missingNumber(nums []int) int {
// 	left, right := 0, len(nums)-1
// 	for left <= right {
// 		mid := (left + right) / 2
// 		if mid == nums[mid] {
// 			left = mid + 1
// 		} else {
// 			right = mid - 1
// 		}
// 	}
// 	return left
// }

// func main() {
// 	nums := []int{0}
// 	ans := missingNumber(nums)
// 	fmt.Println(ans)
// }

package main

import (
	"fmt"
)

func main() {
	ch := make(chan int)
	ch <- 10
	fmt.Println(ch)
}
