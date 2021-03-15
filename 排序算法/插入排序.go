package main

/*
* 1. 把待排序数组分为已排序和未排序两部分，初始时把第一个元素认为是已排好序的
* 2. 从第二个元素开始，在已排好序的子数组中寻找合适的位置插入该位置
* 3. 重复上述过程知道最后一个元素被插入
 */
func InsertSort(nums []int) []int {
	for i := 1; i < len(nums); i++ {
		for j := i; j > 0; j-- {
			if nums[j-1] > nums[j] {
				nums[j], nums[j-1] = nums[j-1], nums[j]
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
//	insertSort(nums)
//	elapsed := time.Since(start)
//	fmt.Println(elapsed)
//}
