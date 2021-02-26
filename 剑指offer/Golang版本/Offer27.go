package main

/*
请完成一个函数，输入一个二叉树，该函数输出它的镜像。

示例 1：

输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof

*/

//Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func mirrorTree(root *TreeNode) *TreeNode {
    if root == nil {
    	return root
	}
	mirrorTree(root.Left)
    mirrorTree(root.Right)
    root.Left, root.Right = root.Right, root.Left
    return root
}
