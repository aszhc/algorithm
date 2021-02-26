package main

import "fmt"

//func quickSort2(sortArray []int, left, right int) {
//	if left < right {
//		//key := sortArray[(left+right)/2]
//		key := sortArray[right]
//		i := left
//		j := right
//		for {
//			for sortArray[i] < key {
//				i++
//			}
//			for sortArray[j] > key {
//				j--
//			}
//			if i >= j {
//				break
//			}
//			sortArray[i], sortArray[j] = sortArray[j], sortArray[i]
//		}
//		quickSort2(sortArray, left, i-1)
//		quickSort2(sortArray, j+1, right)
//	}
//}

func quickSort2(arr []int) []int {
	sort(arr, 0, len(arr) - 1)
	return arr
}

func sort(arr []int, low, high int) {
	if low < high {
		pi := partition(arr, low, high)
		sort(arr, low, pi-1)
		sort(arr, pi+1, high)
	}
}

func partition(arr []int, low, high int) int {
	pivot := arr[high]
	i := low-1

	for j := low; j < high; j++ {
		if arr[j] <= pivot {
			i++
			arr[i], arr[j] = arr[j], arr[i]
		}
	}

	arr[i+1], arr[high] = arr[high], arr[i+1]

	return i+1
}

func main() {
	nums := []int{5, 3, 1, 9, 4, 2, 8}
	quickSort2(nums)
	fmt.Println(nums)
}
