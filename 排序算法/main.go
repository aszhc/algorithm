package main

import (
	"fmt"
	"math/rand"
	"time"
)

// 冒泡排序
func bubbleSort(nums []int) {
	for i := 0; i < len(nums); i++ {
		for j := 1; j < len(nums)-i; j++ {
			if nums[j-1] > nums[j] {
				nums[j-1], nums[j] = nums[j], nums[j-1]
			}
		}
	}
	fmt.Println(nums)
}

// 选择排序
func selectSort(nums []int) {
	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			if nums[i] > nums[j] {
				nums[i], nums[j] = nums[j], nums[i]
			}
		}
	}
	fmt.Println(nums)
}

// 插入排序
func insertSort(nums []int) {
	for i := 1; i < len(nums); i++ {
		for j := i; j > 0; j-- {
			if nums[j-1] > nums[j] {
				nums[j-1], nums[j] = nums[j], nums[j-1]
			}
		}
	}
	fmt.Println(nums)
}

// 快速排序
func quickSort(nums []int) {
	sort(nums, 0, len(nums)-1)
	fmt.Println(nums)
}

func sort(nums []int, low, high int) {
	if low < high {
		mid := partition(nums, low, high)
		sort(nums, low, mid-1)
		sort(nums, mid+1, high)
	}
}

func partition(nums []int, low, high int) int {
	pivot := nums[high]
	i := low - 1
	for j := low; j < high; j++ {
		if nums[j] < pivot {
			i++
			nums[i], nums[j] = nums[j], nums[i]
		}
	}
	nums[i+1], nums[high] = nums[high], nums[i+1]
	return i + 1
}

func createNums(n int) []int {
	var nums []int
	rand.Seed(time.Now().Unix())
	for i := 0; i < n; i++ {
		nums = append(nums, rand.Intn(1000))
	}
	return nums
}

func main() {
	nums := createNums(1000)
	start := time.Now()
	quickSort(nums)
	elapsed := time.Since(start)
	fmt.Println(elapsed)
}
