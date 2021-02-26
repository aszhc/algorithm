package main

import "fmt"

/**
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

示例 1：

输入：s = "We are happy."
输出："We%20are%20happy."

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof
**/

func replaceSpace(s string) string {
	var str string
	start := 0
	for key, value := range s{
		if value == ' '{
			str += s[start: key]
			str += "%20"
			start = key + 1
		}
	}
	str += s[start:]
	return str
}

func main() {
	s := "We are happy."
    ans := replaceSpace(s)
	fmt.Println(ans)
}
