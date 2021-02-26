package main

// 从尾到头打印链表

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func reversePrint(head *ListNode) []int {
	count := 0
	for p := head; p != nil; p = p.Next {
		count++
	}
	res := make([]int, count)
	for ; head != nil; head = head.Next {
		res[count-1] = head.Val
		count--
	}
	return res
}

func main() {

}
