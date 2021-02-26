package main

/**
冒泡排序：第一次循环，确定最后一位为最大值；第二次循环，确定倒数第二位为倒数第二大的值；以此类推。。。
两两比较
时间复杂度 O(n^2)
*/

func BubbleSort(nums []int) []int{
	for i := 0; i < len(nums); i++ {
		for j := 1; j < len(nums)-i; j++ {
			if nums[j-1] > nums[j] {
				nums[j], nums[j-1] = nums[j-1], nums[j]
			}
		}
	}
	//fmt.Println(nums)
	return nums
}




//func createNums(n int) []int {
//	var nums []int
//	rand.Seed(time.Now().Unix())
//	for i := 0; i < n; i++ {
//		nums = append(nums, rand.Intn(1000))
//	}
//	return nums
//}
//
//func main() {
//	//nums := []int{9, 4, 5, 1, 22, 8, 4, 7, 0, 2}
//	nums := createNums(10000)
//	start := time.Now()
//	BubbleSort(nums)
//	elapsed := time.Since(start)
//	fmt.Println(elapsed)
//}