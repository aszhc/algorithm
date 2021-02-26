package main

import "fmt"

func reverseLeftWords(s string, n int) string {
	return s[n:] + s[:n]
}

func main() {
	s:="abcdefg"
	k:=2
	ans := reverseLeftWords(s, k)
	fmt.Println(ans)
}
