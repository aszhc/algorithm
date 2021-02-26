package main

// 给定一棵二叉搜索树，请找出其中第k大的节点。
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func kthLargest(root *TreeNode, k int) int {
	if k < 1 {
		return 0
	}
	var res []int
	dfs(root, &res)
	return res[len(res)-k]
}

func dfs(root *TreeNode, res *[]int) {
	if root == nil {
		return
	}
	if root != nil {
		dfs(root.Left, res)
		*res = append(*res, root.Val)
		dfs(root.Right, res)
	}
}

/*
root == nil 就表示为空
root != nil 就表示不为空
*/
