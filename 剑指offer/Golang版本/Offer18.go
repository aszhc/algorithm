package main

/**
给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

返回删除后的链表的头节点。

注意：此题对比原题有改动

示例 1:

输入: head = [4,5,1,9], val = 5
输出: [4,1,9]
解释: 给定你链表中值为5的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof
**/

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func deleteNode(head *ListNode, val int) *ListNode {
	if head == nil {	// 若为空， 则返回空
		return nil
	}
	if head.Val == val {	// 若只有一个节点，则返回该head.Next
		return head.Next
	}
	pre := head
	for pre.Next != nil && pre.Next.Val != val {
		pre = pre.Next
	}
	if pre.Next != nil {
		pre.Next = pre.Next.Next
	}
	return head
}

func main() {

}
