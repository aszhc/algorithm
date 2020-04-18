/**
* @Author: ZhouChuang
* @Date: 2020/4/15 21:09
 */
package main

func removeDuplicates(nums []int) int {
	i := 0
	for j := 1; j < len(nums); j++ {
		if nums[j] != nums[i] {
			i++
			nums[i] = nums[j]
		}
	}
	return i + 1
}

func main() {
	nums := []int{1, 1, 3}
	removeDuplicates(nums)

}
