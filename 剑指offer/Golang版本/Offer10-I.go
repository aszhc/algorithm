package main

import "fmt"

/**
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：
示例 1：

输入：n = 2
输出：1
示例 2：

输入：n = 5
输出：5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof

**/
//func fib(n int) int {
//	if n == 0 || n == 1 {
//		return n
//	}
//	return fib(n-1) + fib(n-2)
//}

func fib(n int) int {
	if n==0 || n==1{
		return n
	}
	dp := make([]int, n+1)
	dp[0] = 0
	dp[1] = 1
	for i:=2;i<=n;i++{
		dp[i]=(dp[i-1]+dp[i-2])%1000000007
	}
	return dp[n]
}

func main() {
	n := 2
	ans := fib(n)
	fmt.Println(ans)
}
