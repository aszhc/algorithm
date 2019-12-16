package main

import "fmt"

func climbStairs(n int) int {
	if n <= 0 {
		return n
	}
	res, last := 1, 1
	for i := 1; i < n; i++ {
		res, last = res+last, res
		fmt.Println(res, last)
	}
	return res
}
func main() {
	end := climbStairs(5)
	fmt.Println(end)
}
