# encoding=utf-8

import sys
MAX = sys.maxsize
primgraph = [
    [MAX, 1, 6, 2, MAX, MAX],
    [1, MAX, 7, 2, MAX, MAX],
    [6, 7, MAX, 9, 4, 3],
    [2, 2, 9, MAX, 7, 6],
    [MAX, MAX, 4, 7, MAX, 3],
    [MAX, MAX, 3, 6, 3, MAX]
]
chararray = ['1', '2', '3', '4', '5', '6']
charlist = []
charlist.append(chararray[0])
mid = []  # mid[i]表示生成树集合中与点i最近的点的编号
lowcost = []  # lowcost[i]表示生成树集合中与点i最近的点构成的边最小权值 ，-1表示i已经在生成树集合中
lowcost.append(-1)
mid.append(0)
n = len(chararray)
for i in range(1, n):  # 初始化mid数组和lowcost数组
    lowcost.append(primgraph[0][i])
    mid.append(0)
sum = 0
for _ in range(1, n):  # 插入n-1个结点
    minid = 0
    min = MAX
    for j in range(1, n):  # 寻找每次插入生成树的权值最小的结点
        if(lowcost[j] != -1 and lowcost[j] < min):
            minid = j
            min = lowcost[j]
    charlist.append(chararray[minid])
    sum += min
    lowcost[minid] = -1
    for j in range(1, n):  # 更新插入结点后lowcost数组和mid数组值
        if(lowcost[j] != -1 and lowcost[j] > primgraph[minid][j]):
            lowcost[j] = primgraph[minid][j]
            mid[j] = minid

print("插入结点顺序："+str(charlist))
print("sum = " + str(sum))