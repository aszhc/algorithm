package main

import (
	"fmt"
)

/**
找出数组中重复的数字。
**/
//func findRepeatNumber(nums []int) int {
//	for i:=0;i<len(nums);i++{
//		for j:=i+1;j<len(nums);j++{
//			if nums[i] == nums[j]{
//				return nums[i]
//			}
//		}
//	}
//	return 0
//}

func findRepeatNumber(nums []int) int {
	n := make(map[int]bool)
	for _, value := range nums {

		if _, ok := n[value]; ok {
			return value
		}
		n[value] = true
	}
	return 0
}

func main() {
	var question = []int{0, 1, 2, 3, 4, 11, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
	ans := findRepeatNumber(question)
	fmt.Println(ans)
}
