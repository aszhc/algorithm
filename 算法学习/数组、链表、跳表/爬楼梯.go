/**
* @Author: ZhouChuang
* @Date: 2020/4/17 22:01
 */
package main

func climbStairs(n int) int {
	if n < 3 {
		return n
	}
	return climbStairs(n-1) + climbStairs(n-2)
}

func main() {
	climbStairs(5)
}
