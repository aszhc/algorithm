package main

import "fmt"

func hammingWeight(num uint32) int {
	n := 0
	nums := fmt.Sprintf("%b", num)  // ** 将num转换为二进制
	for _, char := range nums {
		if char == '1' {
			n++
		}
	}
	return n
}

func main() {
	var num uint32 = 00000000000000000000000000001011
	ans := hammingWeight(num)
	fmt.Println(ans)
}
