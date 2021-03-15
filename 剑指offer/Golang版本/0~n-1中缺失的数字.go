package main

/*
示例 2:

输入: [0,1,2,3,4,5,6,7,9]
输出: 8
// 只有一个缺失
*/

func missingNumber(nums []int) int {
	left, right := 0, len(nums)-1
	for left <= right {
		mid := (left + right) / 2
		if mid == nums[mid] {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	return left
}

// func main() {
// 	nums := []int{0, 1, 2, 3, 4, 5, 6, 7, 9}
// 	ans := missingNumber(nums)
// 	fmt.Println(ans)
// }
