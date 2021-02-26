package main

import (
	"fmt"
	"math/rand"
	"time"
)

func quickSort(a []int) []int {
	if len(a) < 2 {
		return a
	}
	left, right := 0, len(a)-1
	// Pick a pivot
	pivotIndex := rand.Int() % len(a)
	// Move the pivot to the right
	a[pivotIndex], a[right] = a[right], a[pivotIndex]

	// Pile elements smaller than the pivot on the left
	for i := range a {
		if a[i] < a[right] {
			a[i], a[left] = a[left], a[i]
			left++
		}
	}

	// Place the pivot after the last smaller element
	a[left], a[right] = a[right], a[left]

	// Go down the rabbit hole
	quickSort(a[:left])
	quickSort(a[left+1:])
	return a
}

func createNums(n int) []int {
	var nums []int
	rand.Seed(time.Now().Unix())
	for i := 0; i < n; i++ {
		nums = append(nums, rand.Intn(100000))
	}
	return nums
}

func main() {
	//nums := []int{9, 4, 5, 1, 22, 8, 4, 7, 0, 2}
	nums := createNums(1000000)
	start := time.Now()
	quickSort(nums)
	//sort.Ints(nums)
	elapsed := time.Since(start)
	fmt.Println(elapsed)
}
