package main

import "fmt"

/**
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

示例 1:

输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof
**/

func printNumbers(n int) []int {
	var res []int
	var max int
	for n > 0 {
		max = max*10 + 9
		n--
	}
	for i := 1; i <= max; i++ {
		res = append(res, i)
	}
	return res
}

func main() {
	n := 2
	ans := printNumbers(n)
	fmt.Println(ans)
}