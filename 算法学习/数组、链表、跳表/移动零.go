package main

import (
	"fmt"
)

func moveZeroes(nums []int) {
	var j = 0
	for i := 0; i < len(nums); i++ {
		if nums[i] != 0 {
			nums[i], nums[j] = nums[j], nums[i]
			j++
		}
		fmt.Println(i)
	}
	fmt.Println(nums)
}

func main() {
	nums := []int{0, 1, 0, 3, 12}
	moveZeroes(nums)

}
