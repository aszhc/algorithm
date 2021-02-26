package main

// 每一轮选出最小的放在最前面， 选择排序
func selectSort(nums []int) []int{
	for i := 0; i < len(nums)-1; i++ {
		for j := i + 1; j < len(nums); j++ {
			if nums[i] > nums[j] {
				nums[j], nums[i] = nums[i], nums[j]
			}
		}
	}
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
//	selectSort(nums)
//	elapsed := time.Since(start)
//	fmt.Println(elapsed)
//}