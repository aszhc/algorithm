# encoding=utf_8

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
mid = []  # 生成树中离i最近点的编号
lowcost = []  # 最小权值，-1表示已经被选中
lowcost.append(-1)
mid.append(0)   # 初始化第一个元素
n = len(chararray)
for i in range(1, n):
    lowcost.append(primgraph[0][i])
    mid.append(0)
sum = 0  # 初始化总和

# print(lowcost)
# print(mid)
for _ in range(1, n):  # 插入其他的结点
    minid = 0
    min = MAX
    for j in range(1, n):  # 每次插入生成树的最小结点
        if (lowcost[j] != -1 and lowcost[j] < min):  # 找出最小值
            minid = j
            min = lowcost[j]
    charlist.append(chararray[minid])
    sum += min
    lowcost[minid] = -1
    for j in range(1, n):
        if (lowcost[j] != -1 and lowcost[j] > primgraph[minid][j]):
            lowcost[j] = primgraph[minid][j]
            mid[j] = minid
print(charlist)
print('sum = ' + str(sum))
